#!/usr/bin/env python3
"""Take a source into this library: from .cache/handoff/ (--file) or by download.

    python3 bin/grab.py URL "Short title" --publisher "UC Office of the President" --published 2026-09-16 \
        [--folder web|legislative] [--license "CC BY 4.0"] [--file "<handed file>"] [--original-only --as "<stem>"]

A government document (a .gov host) or a file with an open license (--license) is
rehosted: the original and a Markdown copy go to raw/<folder>/ with rehost: yes.
Anything else is not rehosted: the files go to .cache/ (git ignores it) so you can
read them and write the source page, and the page links to the URL.

--folder: web (default) for every new document, an approved suggestion included;
legislative for statute and legislative records. A suggestion is not a kind of source:
once approved, it is a document like any other. raw/shared/ holds the documents the
library started with; nothing new goes there. Refuses californiacompute.org and refuses
to overwrite.

--file takes the source from .cache/handoff/ instead of the web: the file that the
consortium's wiki fetched, named in the row's `file:` note. URL is still the row's URL:
it decides rehost and goes in the frontmatter. The date at the start of the file name is
the fetched date. Refuses a handed file whose Markdown copy has fewer than 50 words.

--original-only saves the original file and no Markdown copy, for a rehosted original
whose excerpt page already exists; --as names it exactly (no date prefix), so it pairs
with that excerpt.
"""
import argparse
import datetime
import os
import re
import ssl
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPES = {"application/pdf": "pdf", "text/html": "html", "text/plain": "txt", "application/json": "json",
         "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
         "text/csv": "csv", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
         "application/zip": "zip", "application/x-zip-compressed": "zip"}  # markitdown converts each file in a zip
GOV = re.compile(r"(\.|^)gov$|(\.|^)cccco\.edu$|(\.|^)universityofcalifornia\.edu$|leginfo|billtexts\.s3\.amazonaws\.com")

try:  # python.org's macOS build has no CA store of its own
    import certifi
    TLS = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    TLS = ssl.create_default_context()


def markdown(path):
    hint = ["-x", "html"] if path.lower().endswith(".xml") else []  # a bill's CAML XML holds XHTML
    return subprocess.run([os.path.join(ROOT, ".venv", "bin", "markitdown"), os.path.basename(path)] + hint,
                          cwd=os.path.dirname(path), capture_output=True, text=True, check=True).stdout  # basename: a zip copy prints the path


def main():
    a = argparse.ArgumentParser()
    a.add_argument("url"); a.add_argument("title")
    a.add_argument("--publisher", default="unknown"); a.add_argument("--published", default="unknown")
    a.add_argument("--folder", default="web", choices=["web", "legislative"])
    a.add_argument("--license", default="", help="open license of the file, e.g. CC BY 4.0")
    a.add_argument("--original-only", action="store_true", help="save the original only, no Markdown copy")
    a.add_argument("--as", dest="name", default="", help="exact file stem, no date prefix")
    a.add_argument("--file", default="", help="file name in .cache/handoff/; no download")
    o = a.parse_args()
    host = urllib.parse.urlsplit(o.url).netloc.lower()
    if "californiacompute.org" in host:
        sys.exit("refused: californiacompute.org is the consortium's own website, not research")

    # A Wayback Machine copy (leginfo refuses scripts) is judged by the page it archives.
    m = re.match(r"https?://web\.archive\.org/web/[^/]+/(https?://[^/]+)", o.url)
    if m:
        host = urllib.parse.urlsplit(m.group(1)).netloc.lower()
    rehost = bool(GOV.search(host.split(":")[0]) or o.license)
    today = fetched = datetime.date.today().isoformat()
    if o.file:
        src = os.path.join(ROOT, ".cache", "handoff", os.path.basename(o.file))
        m = re.match(r"\d{4}-\d{2}-\d{2}(?= )", os.path.basename(src))
        if not (m and os.path.isfile(src)):
            sys.exit("refused: no file %s in .cache/handoff/ with a YYYY-MM-DD name" % o.file)
        fetched = m.group(0)
    folder = os.path.join(ROOT, "raw", o.folder) if rehost else os.path.join(ROOT, ".cache", o.folder)
    os.makedirs(folder, exist_ok=True)
    if o.original_only and not rehost:
        sys.exit("refused: --original-only is for rehosted originals (a government host or --license)")
    stem = os.path.join(folder, (o.name or "%s %s" % (fetched, o.title)).replace("/", "-"))
    if os.path.exists(stem + ".md") and not o.original_only:
        sys.exit("exists: %s.md" % stem)

    if o.file:  # fetched once, by the consortium's wiki: never download it again
        ext = os.path.splitext(src)[1].lstrip(".").lower()
        if not o.original_only and len(markdown(src).split()) < 50:
            sys.exit("thin: %s gives fewer than 50 words; do not download it, leave the row approved" % o.file)
        with open(src, "rb") as fh:
            body = fh.read()
    else:
        req = urllib.request.Request(o.url, headers={"User-Agent": "Mozilla/5.0 (CalCompute Research Library)"})
        with urllib.request.urlopen(req, context=TLS, timeout=60) as r:
            body, ctype = r.read(), r.headers.get_content_type()
        ext = TYPES.get(ctype) or sys.exit("unknown content type %s; get it by hand" % ctype)
    if os.path.exists(stem + "." + ext):
        sys.exit("exists: %s.%s" % (stem, ext))
    with open(stem + "." + ext, "wb") as fh:
        fh.write(body)
    if o.original_only:
        print("%s.%s  %d bytes  original only" % (os.path.relpath(stem, ROOT), ext, len(body)))
        return

    md = markdown(stem + "." + ext)
    if len(md.split()) < 50:
        print("WARNING: Markdown copy has only %d words; check it" % len(md.split()))
    fm = ["---", "url: %s" % o.url, "fetched: %s" % fetched, 'publisher: "%s"' % o.publisher,
          "published: %s" % o.published, "original: %s" % os.path.basename(stem + "." + ext)]
    fm += ['license: "%s"' % o.license] if o.license else []
    fm += ["rehost: %s" % ("yes" if rehost else "no"), "---", "",
           "_Markdown copy of %s, made %s. The original is the authority._" % (os.path.basename(stem + "." + ext), today), ""]
    with open(stem + ".md", "w") as fh:
        fh.write("\n".join(fm) + md)
    print("%s.%s  %d words  rehost: %s" % (os.path.relpath(stem, ROOT), ext, len(md.split()), "yes" if rehost else "no"))


if __name__ == "__main__":
    main()
