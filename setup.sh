#!/usr/bin/env bash
# Set up this wiki on a new machine. Safe to run again.
# Needs python3 (3.10 or later). Installs markitdown (Markdown copies of PDF, Word and HTML
# files) and google-auth (bin/drive_push.py) into .venv.
set -euo pipefail
cd "$(dirname "$0")"

python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' \
  || { echo "Python 3.10 or later is necessary." >&2; exit 1; }
[ -d .venv ] || python3 -m venv .venv
.venv/bin/python -m pip install --quiet --upgrade pip
.venv/bin/python -m pip install --quiet 'markitdown[all]' google-auth certifi

echo "Done. Markdown copies: .venv/bin/markitdown <file> > <file>.md"
