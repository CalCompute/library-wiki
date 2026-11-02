#!/usr/bin/env python3
"""Put the library's rehosted originals in the public "CalCompute Library" folder of the "CalCompute Public" Shared Drive.

    python3 bin/drive_push.py --check    # say what would be uploaded; change nothing
    python3 bin/drive_push.py            # upload what is missing, then write raw/drive/.listing.json
    python3 bin/drive_push.py --scaffold # before the Drive exists: list the planned folders and files, no Google

Uploads only original documents (PDF, Word, PowerPoint, Excel), never web pages or Markdown copies:
  - raw/shared/, raw/web/ and raw/human/ originals whose Markdown copy says rehost: yes, to the top folder;
  - raw/legislative/*.pdf to Legislative Sources.
Each upload is tagged with its raw/ path, so it is never uploaded twice. Everything lives in the
CalCompute Library folder of the CalCompute Public Shared Drive, which anyone with the link can view (a Shared Drive's own
root cannot be shared by link); the push makes Legislative Sources inside it when missing.
Then it rewrites two branded Google Docs (bin/gdoc.py), the Drive's navigation:
  - 0 - LIBRARY GUIDE at the top: where to start and what is here, then the table of contents in tabs: every
    source in the library, rehosted or not, with its web address, publisher and tier, and a link to its copy in
    this Drive when there is one (all, by element, legislative);
  - 0 - LEGISLATIVE CONTENTS in Legislative Sources: each legislative record with its CalCompute passages.
The Docs come from wiki/sources/ and raw/legislative/, so a new source reaches them on the next push.
The script adds files, updates their descriptions and rewrites its own Docs. It never edits, moves or
deletes anything a person put in the Drive.
Then it lists the whole Drive into raw/drive/.listing.json and raw/drive/.folders.json, which the
site's Drive browser reads. Runs under .venv (Google's sign-in library); see setup.sh. With --scaffold, the
listing shows the folders and files the push would make, and each file opens its copy on the site.

The service account key is at ~/.config/calcompute-bot/drive-key.json, or the path in WIKI_DRIVE_KEY.
The account must be a Content manager of the Shared Drive.
"""
import datetime
import glob
import hashlib
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV_PY = os.path.join(ROOT, ".venv", "bin", "python")
try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
except ImportError:
    if "--scaffold" in sys.argv:
        pass
    elif os.path.exists(VENV_PY) and os.path.realpath(sys.prefix) != os.path.realpath(os.path.join(ROOT, ".venv")):
        os.execv(VENV_PY, [VENV_PY] + sys.argv)
    else:
        sys.exit("Google's sign-in library is missing. Run ./setup.sh.")
try:
    import certifi
    TLS = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    TLS = ssl.create_default_context()

KEY = os.path.expanduser(os.environ.get("WIKI_DRIVE_KEY", "~/.config/calcompute-bot/drive-key.json"))
DRIVE_NAME = "CalCompute Public"      # the Shared Drive; its root cannot be shared by link
PUBLIC_ROOT = "CalCompute Library"    # the folder in it that anyone with the link can view; everything goes inside
FOLDERS = ("", "Legislative Sources")   # the only places the script may add files: the top folder ("") and one subfolder
GUIDE = "0 - LIBRARY GUIDE"
LEGISLATIVE = "0 - LEGISLATIVE CONTENTS"
GUIDE_NOTES = {
    "Legislative Sources": "The statute and the legislative record of SB 53 and the bills before it, with their CalCompute passages.",
    "0 - LIBRARY GUIDE": "Start here: what this Drive is, and every source in the library with its web address and its copy here when there is one.",
    "0 - LEGISLATIVE CONTENTS": "Each legislative record, with its CalCompute passages word for word.",
}
DOCS = {".pdf": "application/pdf",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}
FOLDER = "application/vnd.google-apps.folder"
GDOC = "application/vnd.google-apps.document"
SITE_URL = "https://research.californiacompute.org"
REPO = "https://github.com/CalCompute/library-wiki"
SUGGEST = "mailto:team@californiacompute.org?subject=Suggested%20reading"
# What a Doc must never name (AGENTS.md, "The Drive stands alone").
OFF_LIMITS = re.compile(r"\bthe agent\b|zulip", re.I)
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December")
DOCS_API = "https://docs.googleapis.com/v1/documents/"
API, UPLOAD = "https://www.googleapis.com/drive/v3", "https://www.googleapis.com/upload/drive/v3"


def token():
    if not os.path.exists(KEY):
        sys.exit("No key at %s." % KEY)
    c = service_account.Credentials.from_service_account_file(KEY, scopes=["https://www.googleapis.com/auth/drive"])
    c.refresh(Request())
    return c.token


def req(tok, method, url, body=None, ctype=None):
    r = urllib.request.Request(url, data=body, method=method, headers=dict(
        [("Authorization", "Bearer " + tok)] + ([("Content-Type", ctype)] if ctype else [])))
    try:
        with urllib.request.urlopen(r, context=TLS, timeout=300) as resp:
            return json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit("Drive said %d: %s" % (e.code, e.read().decode(errors="replace")[:300]))


def get(tok, path, **p):
    p.update(supportsAllDrives="true")
    return req(tok, "GET", "%s/%s?%s" % (API, path, urllib.parse.urlencode(p)))


def multipart(tok, method, url, meta, body, ctype):
    b = "library-boundary"
    data = ("--%s\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n%s\r\n--%s\r\nContent-Type: %s\r\n\r\n"
            % (b, json.dumps(meta), b, ctype)).encode() + body + ("\r\n--%s--" % b).encode()
    return req(tok, method, url, data, "multipart/related; boundary=" + b)


def frontmatter(md):
    s = open(md).read()
    if not s.startswith("---\n"):
        return {}
    block = s[4:s.index("\n---", 4)]
    return {k.strip(): v.strip().strip('"') for k, _, v in (l.partition(":") for l in block.splitlines()) if v}


def candidates():
    """(raw path of the original, Drive folder, Drive name, description) for every document to upload.
    A shared or web copy of a legislative PDF is left out: the copy in Legislative Sources serves both."""
    out = []
    legislative = {md5(p) for p in glob.glob(os.path.join(ROOT, "raw", "legislative", "*.pdf"))}
    for md in sorted(sum((glob.glob(os.path.join(ROOT, "raw", d, "*.md")) for d in ("shared", "web", "human")), [])):
        fm = frontmatter(md)
        orig = os.path.join(os.path.dirname(md), fm.get("original") or os.path.basename(md)[:-3] + ".pdf")
        if fm.get("rehost") == "yes" and os.path.splitext(orig)[1] in DOCS and os.path.exists(orig) and md5(orig) not in legislative:
            title = os.path.splitext(os.path.basename(md))[0].split(" ", 1)[-1]
            date = fm.get("published", "unknown")
            meta = ", ".join(x for x in (fm.get("publisher", ""), "" if date == "unknown" else date) if x and x != "unknown")
            name = "%s (%s)" % (title, meta) if meta else title
            desc = "Original: " + fm.get("url", "") + ("; license: " + fm["license"] if fm.get("license") else "")
            out.append((orig, "", name, desc))
    for pdf in sorted(glob.glob(os.path.join(ROOT, "raw", "legislative", "*.pdf"))):
        url = frontmatter(pdf[:-4] + ".md").get("sourceUrl", "") if os.path.exists(pdf[:-4] + ".md") else ""
        out.append((pdf, "Legislative Sources", os.path.basename(pdf), "Original: " + url if url else ""))
    return out


def drive_id(tok):
    drives = [d for d in get(tok, "drives", pageSize=100, fields="drives(id,name)").get("drives", []) if d["name"] == DRIVE_NAME]
    if not drives:
        sys.exit("The service account is not a member of the %s Shared Drive." % DRIVE_NAME)
    return drives[0]["id"]


def folder_in(tok, did, parent, name, check):
    """The folder `name` directly in `parent`; created (and so shared like its parent) when missing."""
    r = get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true",
            q="name = '%s' and '%s' in parents and mimeType = '%s' and trashed = false" % (name, parent, FOLDER),
            fields="files(id,capabilities(canAddChildren))")["files"]
    if r:
        return r[0]
    print("%s folder %s" % ("would create" if check else "create", name))
    if check:
        return {"id": None, "capabilities": {"canAddChildren": True}}
    f = req(tok, "POST", "%s/files?supportsAllDrives=true&fields=id,capabilities(canAddChildren)" % API,
            json.dumps({"name": name, "mimeType": FOLDER, "parents": [parent]}).encode(), "application/json")
    return f


def drive_state(tok, did, check=False):
    """The public root's id; folder ids, and every file in the two folders with its checksum and tag."""
    root = get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true",
               q="name = '%s' and '%s' in parents and mimeType = '%s' and trashed = false" % (PUBLIC_ROOT, did, FOLDER), fields="files(id)")["files"]
    if not root:
        sys.exit("No %s folder at the top of the %s Shared Drive. Make it and share it as Anyone with the link: Viewer." % (PUBLIC_ROOT, DRIVE_NAME))
    root = root[0]["id"]
    folders, files = {}, {}
    for name in FOLDERS:
        folders[name] = get(tok, "files/" + root, fields="id,capabilities(canAddChildren)") if not name else folder_in(tok, did, root, name, check)
        if not folders[name]["id"]:
            files[name] = []
            continue
        files[name] = get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true", pageSize=1000,
                          q="'%s' in parents and trashed = false" % folders[name]["id"],
                          fields="files(id,name,md5Checksum,webViewLink,appProperties,description)")["files"]
    return root, folders, files


def write_listing(tok, did, root):
    """raw/drive/.listing.json (every folder and file under the public root, with its path) and raw/drive/.folders.json (path: id)."""
    items, ids, stack = [], {PUBLIC_ROOT: root}, [(root, PUBLIC_ROOT)]
    while stack:
        fid, path = stack.pop()
        r = get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true", pageSize=1000,
                q="'%s' in parents and trashed = false" % fid,
                fields="files(id,name,mimeType,modifiedTime,webViewLink,appProperties)")["files"]
        for f in r:
            folder = f["mimeType"] == FOLDER
            # copy: the Markdown copy (or excerpt) of an uploaded original, so the site can link its page to this file.
            raw = (f.get("appProperties") or {}).get("raw", "")
            md = os.path.splitext(raw)[0] + ".md" if raw else ""
            items.append(dict(id=f["id"], name=f["name"], path=path, folder=folder, mime=f["mimeType"], modified=f.get("modifiedTime", ""), by="",
                              url=f.get("webViewLink", ""), copy=md if md and os.path.exists(os.path.join(ROOT, md)) else None, bot="writes"))
            if folder:
                ids["%s/%s" % (path, f["name"])] = f["id"]
                stack.append((f["id"], "%s/%s" % (path, f["name"])))
    os.makedirs(os.path.join(ROOT, "raw", "drive"), exist_ok=True)
    with open(os.path.join(ROOT, "raw", "drive", ".listing.json"), "w") as fh:
        json.dump(sorted(items, key=lambda x: (x["path"], x["name"], x["id"])), fh, indent=1, sort_keys=True)
    with open(os.path.join(ROOT, "raw", "drive", ".folders.json"), "w") as fh:
        json.dump(ids, fh, indent=1, sort_keys=True)
    return len(items)


def place(folder):
    return "%s/%s" % (PUBLIC_ROOT, folder) if folder else PUBLIC_ROOT


def write_scaffold():
    """The listing the push would make, before the Drive exists: no ids, and each file links to its copy on the site."""
    items = [dict(id="", name=f, path=PUBLIC_ROOT, folder=True, mime=FOLDER, modified="", by="", url="", copy=None, bot="writes") for f in FOLDERS if f]
    for name, where, url in ((GUIDE, "", "/library/"), (LEGISLATIVE, "/Legislative Sources", "/statute/")):
        items.append(dict(id="", name=name, path=PUBLIC_ROOT + where, folder=False, mime=GDOC, modified="", by="", url=url, copy=None, bot="writes"))
    for path, folder, name, desc in candidates():
        site = "/files/" + "/".join(urllib.parse.quote(seg, safe="") for seg in rel(path).split("/"))
        md = os.path.splitext(rel(path))[0] + ".md"
        items.append(dict(id="", name=name, path=place(folder), folder=False, mime=DOCS[os.path.splitext(path)[1]],
                          modified="", by="", url=site, copy=md if os.path.exists(os.path.join(ROOT, md)) else None, bot="writes"))
    os.makedirs(os.path.join(ROOT, "raw", "drive"), exist_ok=True)
    with open(os.path.join(ROOT, "raw", "drive", ".listing.json"), "w") as fh:
        json.dump(sorted(items, key=lambda x: (x["path"], x["name"])), fh, indent=1, sort_keys=True)
    with open(os.path.join(ROOT, "raw", "drive", ".folders.json"), "w") as fh:
        json.dump({}, fh)
    return len(items)


def docs_batch(tok, fid, requests):
    return req(tok, "POST", DOCS_API + fid + ":batchUpdate", json.dumps({"requests": requests}).encode(), "application/json")


def u16(t):
    return len(t.encode("utf-16-le")) // 2  # Docs indexes count UTF-16 code units


def head(title, lead, contents=True):
    """How every Doc opens: its title, one lead sentence, the date and links to its sections."""
    import gdoc
    t = datetime.date.today()
    return [gdoc.title(title), gdoc.lead(lead), gdoc.updated(("%d" % t.year, "%02d" % t.month, "%02d" % t.day))] + ([gdoc.toc()] if contents else [])


def drive_links(files):
    """raw/ path of an original -> its Drive link; a file with the same bytes as an upload (a legislative
    record that was also shared) links to that upload."""
    up = [f for fo in FOLDERS for f in files[fo] if (f.get("appProperties") or {}).get("raw") and f.get("webViewLink")]
    by_md5 = {f.get("md5Checksum"): f["webViewLink"] for f in up}
    out = {p: by_md5[md5(os.path.join(ROOT, p))] for p in
           (rel(x) for d in ("shared", "web", "human") for x in glob.glob(os.path.join(ROOT, "raw", d, "*.pdf")))
           if md5(os.path.join(ROOT, p)) in by_md5}
    out.update({f["appProperties"]["raw"]: f["webViewLink"] for f in up})
    return out


def sources():
    """Every source page except profiles: (title, web address, publisher, tier, elements, origin, raw original or None)."""
    pub = {}
    for md in glob.glob(os.path.join(ROOT, "wiki", "entities", "*.md")):
        if "publisher" in frontmatter(md).get("tags", ""):
            name = frontmatter(md).get("title") or os.path.basename(md)[:-3]
            for t in re.findall(r"\]\(\.\./sources/([^)]+)\.md\)", open(md).read()):
                pub.setdefault(urllib.parse.unquote(t), name)
    out = []
    for md in sorted(glob.glob(os.path.join(ROOT, "wiki", "sources", "*.md"))):
        fm, body, stem = frontmatter(md), open(md).read(), os.path.basename(md)[:-3]
        if re.search(r"\bpeople\b", fm.get("tags", "")):
            continue  # a profile is about a person; it is on their team page, not here
        cite = (re.search(r"^## Citation\n(.*?)(?=^## |\Z)", body, re.S | re.M) or re.search("$", "")).group(0)
        found = re.search(r"https?://[^\s<>)\]]+", cite)
        url = fm.get("url") or (found.group(0).rstrip(".,;") if found else "")
        orig = None
        m = re.search(r"\]\((?:\.\./)+(raw/[^)]+\.md)\)", body)
        if m:
            raw = os.path.join(ROOT, urllib.parse.unquote(m.group(1)))
            if os.path.exists(raw):
                o = frontmatter(raw).get("original")
                o = os.path.join(os.path.dirname(raw), o) if o else raw[:-3] + ".pdf"
                orig = rel(o) if os.path.exists(o) else None
        if not url:  # no web address: its page in the library
            url = "%s/wiki/sources/%s/" % (SITE_URL, re.sub(r"[\W_]+", "-", stem.lower()).strip("-"))
        out.append((fm.get("title") or stem, url, pub.get(stem, ""), fm.get("tier", ""), re.findall(r"[A-G]", fm.get("elements", "")),
                    fm.get("origin", ""), orig))
    return sorted(out, key=lambda r: r[0].lower())


def contents_tabs(files):
    """The library's table of contents: every source with its web address, publisher, tier and Drive copy.
    Tabs: all sources, by element, legislative sources."""
    import gdoc
    drive = drive_links(files)
    titles = {os.path.basename(f)[0]: os.path.basename(f)[4:-3] for f in glob.glob(os.path.join(ROOT, "wiki", "elements", "? - *.md"))}
    row = lambda r: [[(r[0], {"link": r[1]})], r[2], r[3], [("Open", {"link": drive[r[6]]})] if r[6] in drive else ""]
    cols, widths = ["Source", "Publisher", "Tier", "In this Drive"], [262, 140, 62, 40]
    rows = sources()
    rest = [r for r in rows if r[5] != "legislative"]
    leg = [r for r in rows if r[5] == "legislative"]
    tabs = [("All sources", "📚", head("All sources", "Every source in the CalCompute Research Library. Each title links to the source on the web.", False)
             + [gdoc.p("Copies of government documents and openly licensed files are in this Drive; the last column links to them. "
                       "The library's website has a page for each source with its citation and key claims."),
                gdoc.table(cols, [row(r) for r in rest], widths)])]
    by = head("Sources by element", "The same sources, under each element of the Framework Report they serve.")
    for k in "ABCDEFG":
        here = [row(r) for r in rest if k in r[4]]
        if here:
            by += [gdoc.h1("%s. %s" % (k, titles.get(k, ""))), gdoc.table(cols, here, widths)]
    tabs.append(("By element", "🔠", by))
    tabs.append(("Legislative sources", "⚖️", head("Legislative sources", "SB 53 and the state documents about CalCompute.", False)
                 + [gdoc.table(cols, [row(r) for r in leg], widths)]))
    return tabs, len(rows)


def excerpt_paragraphs(md):
    """The excerpt's body as plain paragraphs, word for word; markdown marks removed, "[...]" kept."""
    body = open(md).read().split("\n---\n", 1)[1]
    out = []
    for block in re.split(r"\n\s*\n", body):
        lines = [re.sub(r"^(\s*>\s*)+", "", l).strip() for l in block.splitlines()]
        text = " ".join(l for l in lines if l)
        text = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"\1", re.sub(r"^#+\s*", "", text).replace("**", ""))
        if text and not re.fullmatch(r"\*?Date Published:.*", text):
            out.append(text)
    return out


def legislative_tabs(files):
    """Every legislative record with its CalCompute passages, oldest first: a list, then one tab each."""
    import gdoc
    drive = drive_links(files)
    docs = []
    for md in glob.glob(os.path.join(ROOT, "raw", "legislative", "*.md")):
        if os.path.basename(md) == "README.md":
            continue
        fm = frontmatter(md)
        url, stem = fm.get("sourceUrl", ""), os.path.basename(md)[:-3]
        title = fm.get("title", stem).replace(" — ", ": ")
        docs.append((fm.get("publishedDate", ""), title, drive.get("raw/legislative/%s.pdf" % stem), url, md))
    docs.sort()
    a = lambda href, text: [(text, {"link": href, "bold": True})] if href else [(text, {"bold": True})]
    rows = [[a(copy or src, title), date, [("Official source", {"link": src})] if src else ""] for date, title, copy, src, md in docs]
    first = head("Legislative sources", "SB 53 and the state documents about CalCompute, with their CalCompute passages.", False)
    first += [gdoc.p("Passages are word for word. [...] marks text left out. Each document has its own tab, oldest first. "
                     "A title links to the copy in this Drive when there is one."),
              gdoc.h1("Documents"), gdoc.table(["Document", "Date", "Source"], rows, [300, 84, 120])]
    tabs, seen = [("Documents", "📜", first)], set()
    for date, title, copy, src, md in docs:
        name = re.sub(r"\s*\(.*?\)", "", title)
        name = (name[:44] + "...") if len(name) > 47 else name
        if name in seen:  # tab titles must be unique: two analyses share a name
            name = name[:34].rstrip(". ") + " " + date
        seen.add(name)
        links = ([("The copy in this Drive", {"link": copy})] if copy else []) + ([(" · ", {})] if copy and src else []) \
            + ([("Official source", {"link": src})] if src else [])
        blocks = [gdoc.title(title), gdoc.lead(date)] + ([gdoc.p(links)] if links else [])
        blocks += [gdoc.h1("CalCompute passages"), gdoc.quote(excerpt_paragraphs(md))]
        tabs.append((name, None, blocks))
    return tabs, len(docs)


def guide_tabs(tok, did, root, files):
    """The library guide: where to start and what is here, then the table of contents as its other tabs."""
    import gdoc
    kids = lambda pid: sorted(get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true", pageSize=500,
                                  q="'%s' in parents and trashed = false" % pid, fields="files(id,name,mimeType,webViewLink,appProperties)")["files"],
                              key=lambda f: (f["mimeType"] != FOLDER, f["mimeType"] != GDOC, f["name"].lower()))
    tag = lambda f: (f.get("appProperties") or {}).get("library")
    link = lambda f, bold=False: [(f["name"], {"link": f["webViewLink"], "bold": bold})]
    top = [f for f in kids(root) if tag(f) != "guide"]
    folders = [f for f in top if f["mimeType"] == FOLDER]
    inside = {f["name"]: kids(f["id"]) for f in folders}
    start = [[[(t, {"bold": True})], w] for t, w in (
        ("All sources (tab)", "Every source in the library, A to Z. Each title links to the source on the web; the last column links to its copy here."),
        ("By element (tab)", "The same sources under each element of the Framework Report they serve."),
        ("Legislative sources (tab)", "SB 53 and the state documents about CalCompute."))]
    start += [[link(c, True), GUIDE_NOTES[c["name"]]] for k in inside.values() for c in k if tag(c) == "legislative"]
    start += [[[("The library's website", {"link": SITE_URL, "bold": True})], "A page for each source, with its citation and key claims, reading lists by element, and search."],
              [[("The library's files on GitHub", {"link": REPO, "bold": True})], "Every page of the library as plain text, and how it is kept."],
              [[("Suggest reading", {"link": SUGGEST, "bold": True})], "Write to team@californiacompute.org with the subject \"Suggested reading\". A consortium member reads each suggestion."]]
    blocks = head("CalCompute Research Library", "How to find and use the library's public documents.")
    blocks += [gdoc.h1("Start here"), gdoc.table(["Where", "What it is"], start, [190, 314]), gdoc.h1("In this Drive")]
    blocks += [gdoc.h2("Original documents"), gdoc.p("Government documents and files with an open license, at the top of this Drive.")]
    blocks += [gdoc.li(link(c)) for c in top if c["mimeType"] != FOLDER]
    for f in folders:
        blocks.append(gdoc.h2(f["name"]))
        if GUIDE_NOTES.get(f["name"]):
            blocks.append(gdoc.p(GUIDE_NOTES[f["name"]]))
        blocks += [gdoc.li(link(c)) for c in inside[f["name"]]]
    blocks += [gdoc.h1("What this is")] + [gdoc.li(x) for x in (
        "The CalCompute Research Library collects public research sources for the CalCompute Framework Report that California Government Code section 11546.8 (SB 53) asks for. It reports what the sources say. It is not a position of the consortium.",
        "This Drive holds copies of government documents and openly licensed files only. The pages for other sources link to the publisher.",
        "The library is a tool to navigate and explore the research. The consortium does not use AI to write the CalCompute Framework Report.",
        "The consortium's calls, recordings and communications are not here.")]
    tabs, n = contents_tabs(files)
    return [("Library guide", "🧭", blocks)] + tabs, n


def refused(tabs):
    """The first line that names what must not reach the Drive, or None."""
    import gdoc
    for n, line in enumerate("\n".join(gdoc.text_of(b) for _, _, b in tabs).splitlines(), 1):
        if OFF_LIMITS.search(re.sub(r"https?://\S+", "", line)):
            return "line %d: %s" % (n, line.strip()[:100])
    return None


def tagged(tok, did, tag):
    return get(tok, "files", corpora="drive", driveId=did, includeItemsFromAllDrives="true",
               q="appProperties has { key='library' and value='%s' } and trashed = false" % tag, fields="files(id,name,webViewLink)")["files"]


def push_docs(tok, did, root, folders, files, check):
    """Write the two Docs (made once, rewritten on every push), the guide last so it lists the other."""
    import gdoc
    jobs = [(LEGISLATIVE, "legislative", folders["Legislative Sources"]["id"], lambda: legislative_tabs(files)),
            (GUIDE, "guide", root, lambda: guide_tabs(tok, did, root, files))]
    for name, tag, parent, build in jobs:
        have = tagged(tok, did, tag)
        tabs, n = build()
        why = refused(tabs)
        if why:
            print("NOT PUSHED %s. It names what must not reach the Drive, %s" % (name, why))
            continue
        if check:
            print("%s %s, %d entries" % ("would rewrite" if have else "would create", name, n))
            continue
        f = have[0] if have else multipart(tok, "POST", UPLOAD + "/files?uploadType=multipart&supportsAllDrives=true&fields=id",
                                           {"name": name, "parents": [parent], "mimeType": GDOC, "appProperties": {"library": tag}},
                                           b" ", "text/markdown")
        gdoc.render(tok, f["id"], tabs)
        print("%s, %d entries: %s" % (name, n, get(tok, "files/" + f["id"], fields="webViewLink")["webViewLink"]))


def rel(p):
    return os.path.relpath(p, ROOT)


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def main():
    if "--scaffold" in sys.argv:
        print("scaffold: listed %d planned items in raw/drive/.listing.json" % write_scaffold())
        return
    check = "--check" in sys.argv
    tok = token()
    did = drive_id(tok)
    root, folders, files = drive_state(tok, did, check)
    up = [(path, folder, name, desc) for path, folder, name, desc in candidates()
          if not any(f.get("appProperties", {}).get("raw") == rel(path) or f.get("md5Checksum") == md5(path) for f in files[folder])]
    for path, folder, name, desc in up:
        print("%s %-20s %s  <-  %s" % ("would upload" if check else "upload", folder or "top folder", name, rel(path)))
    if not check and up:
        for name in {u[1] for u in up}:
            if not folders[name]["capabilities"]["canAddChildren"]:
                sys.exit("The service account cannot add files to %s." % name)
        for path, folder, name, desc in up:
            f = multipart(tok, "POST", UPLOAD + "/files?uploadType=multipart&supportsAllDrives=true&fields=id,name,webViewLink,md5Checksum,appProperties,description",
                          {"name": name, "parents": [folders[folder]["id"]], "description": desc,
                           "appProperties": {"library": "pushed", "raw": rel(path)}},
                          open(path, "rb").read(), DOCS[os.path.splitext(path)[1]])
            files[folder].append(f)
            print("   %s" % f["webViewLink"])
    want = {rel(path): desc for path, folder, name, desc in candidates()}
    for folder in FOLDERS:
        for f in files[folder]:
            raw = f.get("appProperties", {}).get("raw")
            if raw in want and f.get("description", "") != want[raw]:
                print("%s description: %s" % ("would update" if check else "update", f["name"][:70]))
                if not check:
                    req(tok, "PATCH", "%s/files/%s?supportsAllDrives=true&fields=id" % (API, f["id"]),
                        json.dumps({"description": want[raw]}).encode(), "application/json")
    push_docs(tok, did, root, folders, files, check)
    if not check:
        print("listed %d items in raw/drive/.listing.json" % write_listing(tok, did, root))


if __name__ == "__main__":
    main()
