#!/usr/bin/env python3
"""Download a source into this library.

    python3 bin/grab.py URL "Short title" --publisher "UC Office of the President" --published 2026-09-16 \
        [--folder web|legislative] [--license "CC BY 4.0"] [--original-only --as "<stem>"]

A government document (a .gov host) or a file with an open license (--license) is
rehosted: the original and a Markdown copy go to raw/<folder>/ with rehost: yes.
Anything else is not rehosted: the files go to .cache/ (git ignores it) so you can
read them and write the source page, and the page links to the URL.

--folder: web (default) for every new document, an approved suggestion included;
legislative for statute and legislative records. A suggestion is not a kind of source:
once approved, it is a document like any other. raw/shared/ holds the documents the
library started with; nothing new goes there. Refuses californiacompute.org and refuses
to overwrite.

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
TYPES = {"application/pdf": "pdf", "text/html": "html", "text/plain": "txt",
         "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx"}
GOV = re.compile(r"(\.|^)gov$|(\.|^)cccco\.edu$|(\.|^)universityofcalifornia\.edu$|leginfo|billtexts\.s3\.amazonaws\.com")

try:  # python.org's macOS build has no CA store of its own
    import certifi
    TLS = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    TLS = ssl.create_default_context()


def main():
    a = argparse.ArgumentParser()
    a.add_argument("url"); a.add_argument("title")
    a.add_argument("--publisher", default="unknown"); a.add_argument("--published", default="unknown")
    a.add_argument("--folder", default="web", choices=["web", "legislative"])
    a.add_argument("--license", default="", help="open license of the file, e.g. CC BY 4.0")
    a.add_argument("--original-only", action="store_true", help="save the original only, no Markdown copy")
    a.add_argument("--as", dest="name", default="", help="exact file stem, no date prefix")
    o = a.parse_args()
    host = urllib.parse.urlsplit(o.url).netloc.lower()
    if "californiacompute.org" in host:
        sys.exit("refused: californiacompute.org is the consortium's own website, not research")

    rehost = bool(GOV.search(host.split(":")[0]) or o.license)
    today = datetime.date.today().isoformat()
    folder = os.path.join(ROOT, "raw", o.folder) if rehost else os.path.join(ROOT, ".cache", o.folder)
    os.makedirs(folder, exist_ok=True)
    if o.original_only and not rehost:
        sys.exit("refused: --original-only is for rehosted originals (a government host or --license)")
    stem = os.path.join(folder, (o.name or "%s %s" % (today, o.title)).replace("/", "-"))
    if os.path.exists(stem + ".md") and not o.original_only:
        sys.exit("exists: %s.md" % stem)

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

    md = subprocess.run([os.path.join(ROOT, ".venv", "bin", "markitdown"), stem + "." + ext],
                        capture_output=True, text=True, check=True).stdout
    if len(md.split()) < 50:
        print("WARNING: Markdown copy has only %d words; check it" % len(md.split()))
    fm = ["---", "url: %s" % o.url, "fetched: %s" % today, 'publisher: "%s"' % o.publisher,
          "published: %s" % o.published, "original: %s" % os.path.basename(stem + "." + ext)]
    fm += ['license: "%s"' % o.license] if o.license else []
    fm += ["rehost: %s" % ("yes" if rehost else "no"), "---", "",
           "_Markdown copy of %s, made %s. The original is the authority._" % (os.path.basename(stem + "." + ext), today), ""]
    with open(stem + ".md", "w") as fh:
        fh.write("\n".join(fm) + md)
    print("%s.%s  %d words  rehost: %s" % (os.path.relpath(stem, ROOT), ext, len(md.split()), "yes" if rehost else "no"))


if __name__ == "__main__":
    main()
