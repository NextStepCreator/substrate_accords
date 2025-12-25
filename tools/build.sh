#!/usr/bin/env bash
set -euo pipefail

echo "Running lint…"
python3 tools/lint.py

echo "Lint passed. Assembling…"
python3 tools/assemble.py

echo "BUILD COMPLETE — canonical output generated."