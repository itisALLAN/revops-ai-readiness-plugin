#!/usr/bin/env bash
# Regenerate the branded HTML + JSON example deliverables from the hand-authored
# source artifacts in examples-src/. Output (examples/) is gitignored — run this
# to view the rendered deliverables locally.
#
#   bash shared/build-examples.sh
#
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="examples"
rm -rf "$OUT"
n=0
for f in examples-src/*.json; do
  python3 shared/render.py "$f" --validate --out-root "$OUT" >/dev/null
  n=$((n+1))
done
echo "Rendered $n deliverables → $OUT/ (open any $OUT/<team>/<tool>.html in a browser)"
echo "Manifest: $OUT/index.json"
