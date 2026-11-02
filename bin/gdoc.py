"""Branded Google Docs for the CalCompute Library Drive, written through the Google Docs API.

bin/drive_push.py builds each navigation Doc (the library guide, the library contents and the
legislative contents) as tabs of blocks, and render() writes them. One look for all of them: CalCompute's colours,
the brand's fallback fonts (Georgia for headings, Arial for text; Lyon Text and Kievit are licensed
and not in Docs), a header with the wordmark, a title, a lead sentence, an Updated date chip and links
to the sections. Tables replace lists with more than one fact per item.

Blocks, made with the helpers below:
  title(text)  lead(text)  h1(text)  h2(text)  h3(text)  p(runs)  li(runs)  quote(paragraphs)
  toc()  updated(ymd)  table(header, rows, widths)
Runs are a string, or a list of (text, style) with style keys bold, muted, link (a URL).
"""
import json
import os
import ssl
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drive_push import DOCS_API, MONTHS, TLS, docs_batch, req, u16  # noqa: E402

BRAND = {"blue": "#1295d8", "navy": "#005581", "dark": "#002033", "wash": "#bde3f6", "off": "#f4f7fb",
         "gold": "#ffb511", "warm": "#dbd5cd", "gray": "#4c4c4c"}  # CaliforniaCompute.org site/src/styles/tokens.css
LOGO = "https://research.californiacompute.org/images/brand/calcompute-wordmark-sticker.png"  # white on blue, as the website header
MARK = "CalCompute Research Library"  # the header when the wordmark image cannot be fetched
TABLE_MARK = "⁣T%d⁣"  # an invisible marker paragraph where a table goes


def color(h):
    return {"color": {"rgbColor": {"red": int(h[1:3], 16) / 255, "green": int(h[3:5], 16) / 255, "blue": int(h[5:7], 16) / 255}}}


def pt(n):
    return {"magnitude": n, "unit": "PT"}


def runs(x):
    return [(x, {})] if isinstance(x, str) else [(t, s or {}) for t, s in x]


def title(text):
    return ("TITLE", runs(text))


def lead(text):
    return ("SUBTITLE", runs(text))


def h1(text):
    return ("HEADING_1", runs(text))


def h2(text):
    return ("HEADING_2", runs(text))


def h3(text):
    return ("HEADING_3", runs(text))


def p(x):
    return ("NORMAL_TEXT", runs(x))


def li(x):
    return ("LI", runs(x))


def quote(paragraphs):
    return ("QUOTE", [runs(x) for x in paragraphs])


def toc():
    return ("TOC",)


def updated(ymd):
    return ("DATE", ymd)


def table(header, rows, widths=None):
    return ("TABLE", header, [[runs(c) for c in r] for r in rows], widths)


def md_blocks(md):
    """Blocks from simple Markdown: "# " and "## " headings, "- " or "1. " items, "| a | b |" tables
    (the first row is the header), and paragraphs. **bold** and [text](url) become runs."""
    import re
    def rs(t):
        out = []
        for part in re.split(r"(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))", t):
            m = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", part)
            if m:
                out.append((m.group(1), {"link": m.group(2)}))
            elif part.startswith("**") and part.endswith("**"):
                out.append((part[2:-2], {"bold": True}))
            elif part:
                out.append((part, {}))
        return out
    blocks, rows = [], []
    for line in md.strip().split("\n") + [""]:
        line = line.strip()
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip("|").split("|")])
            continue
        if rows:
            blocks.append(table(rows[0], [[rs(c) for c in r] for r in rows[1:]]))
            rows = []
        if line.startswith("## "):
            blocks.append(h2(line[3:]))
        elif line.startswith("# "):
            blocks.append(h1(line[2:]))
        elif re.match(r"(- |\d+\. )", line):
            blocks.append(li(rs(re.sub(r"^(- |\d+\. )", "", line))))
        elif line:
            blocks.append(p(rs(line)))
    return blocks


def text_of(blocks):
    """All the words in the blocks, for the check of what must not reach the Drive. Quotes are
    left out: they are what someone else wrote."""
    out = []
    for b in blocks:
        if b[0] == "TABLE":
            out += ["\t".join(b[1])] + ["\t".join("".join(t for t, _ in c) for c in r) for r in b[2]]
        elif b[0] not in ("QUOTE", "TOC", "DATE"):
            out.append("".join(t for t, _ in b[1]))
    return "\n".join(out)


_logo = None


def logo_ok():
    """True when the website serves the wordmark PNG (Docs can insert only a public PNG, JPEG or GIF)."""
    global _logo
    if _logo is None:
        try:
            r = urllib.request.Request(LOGO, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})  # Cloudflare refuses Python's default agent
            with urllib.request.urlopen(r, context=TLS, timeout=20) as resp:
                _logo = resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image/png")
        except Exception:
            _logo = False
    return _logo


def get(tok, fid):
    return req(tok, "GET", DOCS_API + fid + "?includeTabsContent=true")


def batch(tok, fid, reqs, size=400):
    for i in range(0, len(reqs), size):
        docs_batch(tok, fid, reqs[i:i + size])


def para_text(e):
    return "".join(r.get("textRun", {}).get("content", "") for r in e["paragraph"]["elements"])


def body(tab):
    return tab["documentTab"]["body"]["content"]


def setup_tabs(tok, fid, specs):
    """The Doc's tabs, in order, with these titles and icons; their bodies empty. Returns the tab ids."""
    doc = get(tok, fid)
    first = doc["tabs"][0]
    tid = first["tabProperties"]["tabId"]
    reqs = [{"deleteTab": {"tabId": t["tabProperties"]["tabId"]}} for t in doc["tabs"][1:]]
    end = body(first)[-1]["endIndex"]
    if end > 2:
        reqs.append({"deleteContentRange": {"range": {"tabId": tid, "startIndex": 1, "endIndex": end - 1}}})
    props = {"tabId": tid, "title": specs[0][0]}
    if specs[0][1]:
        props["iconEmoji"] = specs[0][1]
    reqs.append({"updateDocumentTabProperties": {"tabProperties": props, "fields": ",".join(k for k in props if k != "tabId")}})
    for i, (name, emoji) in enumerate(specs[1:], 1):
        props = {"title": name, "index": i}
        if emoji:
            props["iconEmoji"] = emoji
        reqs.append({"addDocumentTab": {"tabProperties": props}})
    reply = docs_batch(tok, fid, reqs)
    return [tid] + [r["addDocumentTab"]["tabProperties"]["tabId"] for r in reply.get("replies", []) if "addDocumentTab" in r]


def write_text(tok, fid, tab, blocks):
    """Every paragraph of the tab in one insert, then its styles. A table is a marker paragraph for now.
    Returns the tables, in order, and the tab's headings for its "On this page" list."""
    heads = [b[1] for b in blocks if b[0] in ("HEADING_1", "HEADING_2")]
    paras, tables = [], []  # (named style, runs, kind)
    for b in blocks:
        if b[0] == "TOC" and heads:
            paras.append(("HEADING_3", [("On this page", {})], "toc-head"))
            paras += [("NORMAL_TEXT", [("".join(t for t, _ in h), {})], "toc") for h in heads]
        elif b[0] == "DATE":
            y, m, d = b[1]
            paras.append(("NORMAL_TEXT", [("Updated ", {"muted": True}), ("%s %d, %s" % (MONTHS[int(m) - 1], int(d), y), {"date": b[1]})], "date"))
        elif b[0] == "QUOTE":
            paras += [("NORMAL_TEXT", r, "quote") for r in b[1]]
        elif b[0] == "TABLE":
            paras.append(("NORMAL_TEXT", [(TABLE_MARK % len(tables), {})], "table"))
            tables.append(b)
        elif b[0] == "LI":
            paras.append(("NORMAL_TEXT", b[1], "li"))
        elif b[0] != "TOC":
            paras.append((b[0], b[1], ""))
    text, at, reqs, later = "", 1, [], []
    for style, rs, kind in paras:
        line = "".join(t.replace("\n", " ") for t, _ in rs)
        n = u16(line) + 1
        rng = {"tabId": tab, "startIndex": at, "endIndex": at + n}
        ps = {"namedStyleType": style, "shading": {}, "borderLeft": {}, "indentStart": pt(0)}
        fields = "namedStyleType,indentStart"
        if kind == "quote":
            ps.update(shading={"backgroundColor": color(BRAND["off"])}, indentStart=pt(18),
                      borderLeft={"color": color(BRAND["blue"]), "width": pt(3), "padding": pt(8), "dashStyle": "SOLID"})
            fields += ",shading,borderLeft"
        reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": ps, "fields": fields}})
        if kind in ("li", "toc"):
            later.append({"createParagraphBullets": {"range": dict(rng, endIndex=at + n - 1),  # not into the next paragraph
                                                     "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
        off = at
        for t, s in rs:
            k = u16(t.replace("\n", " "))
            ts, f = {}, []
            if s.get("bold"):
                ts["bold"], f = True, f + ["bold"]
            if s.get("muted"):
                ts["foregroundColor"], f = color(BRAND["gray"]), f + ["foregroundColor"]
            if s.get("link"):
                ts["link"], f = {"url": s["link"]}, f + ["link"]
            if f and k:
                reqs.append({"updateTextStyle": {"range": {"tabId": tab, "startIndex": off, "endIndex": off + k},
                                                 "textStyle": ts, "fields": ",".join(f)}})
            off += k
        text, at = text + line + "\n", at + n
    clear = [{"updateTextStyle": {"range": {"tabId": tab, "startIndex": 1, "endIndex": at}, "textStyle": {},
                                  "fields": "bold,italic,underline,link,foregroundColor,backgroundColor,fontSize,weightedFontFamily"}},
             {"deleteParagraphBullets": {"range": {"tabId": tab, "startIndex": 1, "endIndex": at + 1}}}]  # through the tab's last paragraph
    batch(tok, fid, [{"insertText": {"location": {"tabId": tab, "index": 1}, "text": text}}] + clear + reqs + later)
    return tables, ["".join(t for t, _ in h) for h in heads]


def tab_of(doc, tid):
    return next(t for t in doc["tabs"] if t["tabProperties"]["tabId"] == tid)


def write_tables(tok, fid, tab, tables):
    """Each marker paragraph becomes a table: header row in the brand's light blue, warm grey rules,
    the header row pinned, links and bold in the cells."""
    if not tables:
        return
    marks = []
    for e in body(tab_of(get(tok, fid), tab)):
        if "paragraph" in e and para_text(e).strip().startswith("⁣T"):
            marks.append((int(para_text(e).strip()[2:-1]), e["startIndex"], e["endIndex"]))
    reqs = []
    for i, s, e in sorted(marks, key=lambda m: -m[1]):
        _, header, rows, _ = tables[i]
        reqs += [{"deleteContentRange": {"range": {"tabId": tab, "startIndex": s, "endIndex": e - 1}}},
                 {"insertTable": {"rows": len(rows) + 1, "columns": len(header), "location": {"tabId": tab, "index": s}}}]
    batch(tok, fid, reqs)
    found = [e for e in body(tab_of(get(tok, fid), tab)) if "table" in e]
    cells, fills = [], []
    for spec, e in zip([tables[i] for i, _, _ in sorted(marks)], found):
        grid = [[[(t, {"bold": True, "head": True})] for t in spec[1]]] + spec[2]
        for r, row in enumerate(e["table"]["tableRows"]):
            for c, cell in enumerate(row["tableCells"]):
                text = "".join(t for t, _ in grid[r][c]).replace("\n", " ")
                if text:
                    fills.append((cell["content"][0]["startIndex"], text))
    batch(tok, fid, [{"insertText": {"location": {"tabId": tab, "index": i}, "text": t}} for i, t in sorted(fills, key=lambda f: -f[0])])
    found = [e for e in body(tab_of(get(tok, fid), tab)) if "table" in e]
    reqs = []
    line = {"color": color(BRAND["warm"]), "width": pt(0.5), "dashStyle": "SOLID"}
    for spec, e in zip([tables[i] for i, _, _ in sorted(marks)], found):
        _, header, rows, widths = spec
        start = {"tabId": tab, "index": e["startIndex"]}
        every = {"tableCellLocation": {"tableStartLocation": start, "rowIndex": 0, "columnIndex": 0},
                 "rowSpan": len(rows) + 1, "columnSpan": len(header)}
        reqs += [{"updateTableCellStyle": {"tableRange": every, "fields": "borderTop,borderBottom,borderLeft,borderRight,paddingTop,paddingBottom,paddingLeft,paddingRight",
                                           "tableCellStyle": {"borderTop": line, "borderBottom": line, "borderLeft": line, "borderRight": line,
                                                              "paddingTop": pt(3), "paddingBottom": pt(3), "paddingLeft": pt(5), "paddingRight": pt(5)}}},
                 {"updateTableCellStyle": {"tableRange": dict(every, rowSpan=1), "fields": "backgroundColor",
                                           "tableCellStyle": {"backgroundColor": color(BRAND["wash"])}}},
                 {"pinTableHeaderRows": {"tableStartLocation": start, "pinnedHeaderRowsCount": 1}},
                 {"updateTextStyle": {"range": {"tabId": tab, "startIndex": e["startIndex"], "endIndex": e["endIndex"]},
                                      "textStyle": {"fontSize": pt(9.5)}, "fields": "fontSize"}}]
        for c, w in enumerate(widths or []):
            if w:
                reqs.append({"updateTableColumnProperties": {"tableStartLocation": start, "columnIndices": [c],
                                                             "tableColumnProperties": {"widthType": "FIXED_WIDTH", "width": pt(w)}, "fields": "width,widthType"}})
        grid = [[[(t, {"bold": True, "dark": True})] for t in header]] + rows
        for r, row in enumerate(e["table"]["tableRows"]):
            for c, cell in enumerate(row["tableCells"]):
                off = cell["content"][0]["startIndex"]
                for t, s in grid[r][c]:
                    k = u16(t.replace("\n", " "))
                    ts, f = {}, []
                    if s.get("bold"):
                        ts["bold"], f = True, f + ["bold"]
                    if s.get("dark"):
                        ts["foregroundColor"], f = color(BRAND["dark"]), f + ["foregroundColor"]
                    if s.get("muted"):
                        ts["foregroundColor"], f = color(BRAND["gray"]), f + ["foregroundColor"]
                    if s.get("link"):
                        ts["link"], f = {"url": s["link"]}, f + ["link"]
                    if f and k:
                        reqs.append({"updateTextStyle": {"range": {"tabId": tab, "startIndex": off, "endIndex": off + k},
                                                         "textStyle": ts, "fields": ",".join(f)}})
                    off += k
    batch(tok, fid, reqs)


def links_and_chips(tok, fid, tab, heads):
    """"On this page" items link to their headings; the Updated date becomes a date chip."""
    t = tab_of(get(tok, fid), tab)
    ids, reqs, chip = {}, [], None
    for e in body(t):
        if "paragraph" in e and e["paragraph"]["paragraphStyle"].get("headingId"):
            ids.setdefault(para_text(e).strip(), e["paragraph"]["paragraphStyle"]["headingId"])
    for e in body(t):
        if "paragraph" not in e:
            continue
        line = para_text(e).rstrip("\n")
        if e["paragraph"].get("bullet") and line in heads and line in ids:
            reqs.append({"updateTextStyle": {"range": {"tabId": tab, "startIndex": e["startIndex"], "endIndex": e["startIndex"] + u16(line)},
                                             "textStyle": {"link": {"heading": {"id": ids[line], "tabId": tab}}}, "fields": "link"}})
        elif line.startswith("Updated ") and chip is None:
            chip = (e["startIndex"] + u16("Updated "), e["startIndex"] + u16(line), line[8:])
    if chip:
        y = chip[2].split(", ")[1]
        m, d = chip[2].split(", ")[0].split(" ")
        reqs += [{"deleteContentRange": {"range": {"tabId": tab, "startIndex": chip[0], "endIndex": chip[1]}}},
                 {"insertDate": {"location": {"tabId": tab, "index": chip[0]}, "dateElementProperties": {
                     "timestamp": "%s-%02d-%02dT19:00:00Z" % (y, MONTHS.index(m) + 1, int(d)),
                     "dateFormat": "DATE_FORMAT_MONTH_DAY_YEAR_ABBREVIATED", "timeFormat": "TIME_FORMAT_DISABLED", "locale": "en"}}}]
    if reqs:
        batch(tok, fid, reqs)


def brand(tok, fid, tab):
    """The tab's named styles in CalCompute's colours and fonts, its margins, and its header."""
    def style(kind, font, size, hexc, bold=False, above=None, below=None, border=False):
        ts = {"weightedFontFamily": {"fontFamily": font, "weight": 700 if bold else 400}, "fontSize": pt(size),
              "foregroundColor": color(hexc), "bold": bold}
        ps, f = {}, ["namedStyleType", "textStyle"]
        if above is not None:
            ps["spaceAbove"], f = pt(above), f + ["paragraphStyle.spaceAbove"]
        if below is not None:
            ps["spaceBelow"], f = pt(below), f + ["paragraphStyle.spaceBelow"]
        if border:
            ps["borderBottom"] = {"color": color(BRAND["gold"]), "width": pt(2), "padding": pt(4), "dashStyle": "SOLID"}
            f.append("paragraphStyle.borderBottom")
        return {"updateNamedStyle": {"namedStyle": {"namedStyleType": kind, "textStyle": ts, "paragraphStyle": ps},
                                     "fields": ",".join(f), "tabId": tab}}
    reqs = [style("NORMAL_TEXT", "Arial", 10.5, BRAND["navy"]),
            style("TITLE", "Georgia", 26, BRAND["dark"], True, 0, 4),
            style("SUBTITLE", "Arial", 12, BRAND["gray"], False, 0, 10),
            style("HEADING_1", "Georgia", 19, BRAND["dark"], True, 22, 8, border=True),
            style("HEADING_2", "Georgia", 14.5, BRAND["navy"], True, 16, 6),
            style("HEADING_3", "Arial", 11.5, BRAND["blue"], True, 12, 4),
            {"updateDocumentStyle": {"documentStyle": {k: pt(54) for k in ("marginLeft", "marginRight")},
                                     "fields": "marginLeft,marginRight", "tabId": tab}}]
    t = tab_of(get(tok, fid), tab)
    hid = t["documentTab"]["documentStyle"].get("defaultHeaderId")
    if not hid:
        hid = docs_batch(tok, fid, [{"createHeader": {"type": "DEFAULT", "sectionBreakLocation": {"tabId": tab, "index": 0}}}])["replies"][0]["createHeader"]["headerId"]
        t = tab_of(get(tok, fid), tab)
    content = t["documentTab"]["headers"][hid]["content"]
    end = content[-1]["endIndex"]
    seg = {"tabId": tab, "segmentId": hid}
    start = content[0].get("startIndex", 0)
    if end - start > 1:
        reqs.append({"deleteContentRange": {"range": dict(seg, startIndex=start, endIndex=end - 1)}})
    if logo_ok():
        reqs.append({"insertInlineImage": {"uri": LOGO, "location": dict(seg, index=start),
                                           "objectSize": {"height": pt(24), "width": pt(107)}}})
        n = 1
    else:
        reqs.append({"insertText": {"location": dict(seg, index=start), "text": MARK}})
        n = u16(MARK)
        reqs.append({"updateTextStyle": {"range": dict(seg, startIndex=start, endIndex=start + n), "fields": "weightedFontFamily,fontSize,foregroundColor,bold",
                                         "textStyle": {"weightedFontFamily": {"fontFamily": "Georgia", "weight": 700}, "fontSize": pt(10.5),
                                                       "foregroundColor": color(BRAND["blue"]), "bold": True}}})
    reqs.append({"updateParagraphStyle": {"range": dict(seg, startIndex=start, endIndex=start + n + 1), "fields": "borderBottom,spaceBelow",
                                          "paragraphStyle": {"borderBottom": {"color": color(BRAND["gold"]), "width": pt(1.5), "padding": pt(4), "dashStyle": "SOLID"},
                                                             "spaceBelow": pt(6)}}})
    batch(tok, fid, reqs)


def render(tok, fid, tabs):
    """Write tabs [(title, emoji or None, blocks)] into the Doc fid, replacing what is there."""
    ids = setup_tabs(tok, fid, [(t, e) for t, e, _ in tabs])
    for tid, (_, _, blocks) in zip(ids, tabs):
        tables, heads = write_text(tok, fid, tid, blocks)
        write_tables(tok, fid, tid, tables)
        links_and_chips(tok, fid, tid, heads)
        brand(tok, fid, tid)
