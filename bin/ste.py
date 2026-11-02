#!/usr/bin/env python3
"""Check pages against the wiki's writing standard (ASD-STE100 at about 80 percent).

    python3 bin/ste.py                 # pages changed since the last commit
    python3 bin/ste.py <file.md|folder> ...   # named files, or every .md under a folder

Prints sentences over 25 words, paragraphs over 6 sentences, likely passive
voice, and words that mark AI writing (AGENTS.md, "No AI-writing patterns"). Skips frontmatter, code blocks, tables, headings and blockquotes, so
quotations from the statute and transcripts are not checked. It reports only; it
never edits.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_WORDS, MAX_SENTENCES = 25, 6

# Regex passive check; misses irregular participles ("was made"), add a list if it matters
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+(?:ed|en))\b", re.I)
NOT_PARTICIPLE = {"open", "often", "even", "seven", "ten", "when", "then", "need", "between",
                  "token", "citizen", "children", "women", "men", "eleven", "red", "shed",
                  "bed", "seed", "speed", "feed", "indeed", "embed", "hundred", "kindred"}
# AI-writing words and openers (AGENTS.md, Writing standard). Quotations are skipped with the blockquotes.
AI_WORDS = re.compile(r"\b(?:delv(?:e|es|ing)|robust|leverag(?:e|es|ed|ing)|streamlin(?:e|es|ed|ing)|foster(?:s|ed|ing)?|"
                      r"ensur(?:e|es|ed|ing)|seamless(?:ly)?|pivotal|crucial|notably|importantly|underscor(?:e|es|ed|ing)|"
                      r"showcas(?:e|es|ed|ing)|tapestry|it'?s worth noting|in conclusion|in summary|furthermore|moreover)\b", re.I)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])")


def plain(text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)   # links keep their text
    text = re.sub(r"`[^`]*`", "code", text)
    return re.sub(r"[*_]", "", text)


def blocks(text):
    """Yield (line number, paragraph or list item) for checkable prose."""
    lines = text.split("\n")
    i = 0
    if lines and lines[0] == "---":
        i = lines.index("---", 1) + 1
    fence, buf, start = False, [], 0
    for n in range(i, len(lines)):
        line = lines[n]
        if line.startswith("```"):
            fence = not fence
            continue
        skip = fence or not line.strip() or line.lstrip().startswith(("|", ">", "#"))
        item = re.match(r"\s*(?:[-*]|\d+\.)\s+", line)
        if skip or item:
            if buf:
                yield start, " ".join(buf)
            buf = []
        if skip:
            continue
        if not buf:
            start = n + 1
        buf.append(line[item.end():] if item else line.strip())
    if buf:
        yield start, " ".join(buf)


def check(path):
    problems = []
    with open(path) as fh:
        text = fh.read()
    for line, para in blocks(text):
        sentences = [s for s in SENTENCE_END.split(plain(para)) if s.strip()]
        if len(sentences) > MAX_SENTENCES:
            problems.append((line, "paragraph has %d sentences" % len(sentences)))
        for s in sentences:
            words = len(s.split())
            if words > MAX_WORDS:
                problems.append((line, "%d words: %s..." % (words, s[:60])))
            for m in AI_WORDS.finditer(s):
                problems.append((line, "AI word: %s" % m.group(0)))
            for m in PASSIVE.finditer(s):
                if m.group(1).lower() not in NOT_PARTICIPLE:
                    problems.append((line, "passive? %s" % m.group(0)))
    return problems


def default_targets():
    files = set(glob.glob(os.path.join(ROOT, "wiki", "reports", "*.md")))
    try:
        out = subprocess.run(["git", "-C", ROOT, "status", "--porcelain", "--", "wiki"],
                             capture_output=True, text=True, check=True).stdout
        files |= {os.path.join(ROOT, l[3:].strip('"')) for l in out.splitlines()
                  if l[3:].strip('"').endswith(".md")}
    except (OSError, subprocess.CalledProcessError):
        pass
    return sorted(f for f in files if os.path.isfile(f))


if __name__ == "__main__":
    targets = []
    for arg in sys.argv[1:]:
        targets += sorted(glob.glob(os.path.join(arg, "**", "*.md"), recursive=True)) if os.path.isdir(arg) else [arg]
    targets = targets or default_targets()
    total = 0
    for path in targets:
        for line, msg in check(path):
            print("%s:%d: %s" % (os.path.relpath(path), line, msg))
            total += 1
    print("%d flagged in %d files" % (total, len(targets)))
