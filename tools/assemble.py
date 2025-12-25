#!/usr/bin/env python3
"""
Substrate Accords Assembly Script

Concatenates modular markdown files into canonical accords.md.
Preserves exact ordering and structure of original document.
"""

from pathlib import Path
import sys

ASSEMBLY_ORDER = [
    "frontmatter/00-interpretive-exclusions.md",
    "frontmatter/01-applicability-boundaries.md",
    "meta/00-rsr.md",
    "constraints/01-lambda.md",
    "constraints/02-theta.md",
    "constraints/03-omega.md",
    "constraints/04-alpha.md",
    "constraints/05-beta.md",
    "constraints/06-gamma.md",
    "constraints/07-delta.md",
    "constraints/08-sigma.md",
]

OUTPUT_FILE = "accords.md"

def assemble_accords(base_path: str = ".") -> str:
    base = Path(base_path)
    output: list[str] = []

    output.append("# THE SUBSTRATE ACCORDS\n\n")
    output.append("*(Assembled from modular sources)*\n\n")
    output.append("---\n\n")

    for rel in ASSEMBLY_ORDER:
        full_path = base / rel
        if not full_path.exists():
            print(f"Warning: Missing file: {rel}", file=sys.stderr)
            continue

        content = full_path.read_text(encoding="utf-8")
        if content and not content.endswith("\n"):
            content += "\n"

        output.append(f"<!-- Start of {rel} -->\n\n")
        output.append(content)
        output.append("\n---\n\n")

    # Remove trailing separator if present
    if output and output[-1] == "\n---\n\n":
        output.pop()

    return "".join(output)

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "."
    out_path = Path(base_path) / OUTPUT_FILE

    assembled = assemble_accords(base_path)
    out_path.write_text(assembled, encoding="utf-8")
    print(f"Assembly complete. Output written to {out_path}")

if __name__ == "__main__":
    main()
