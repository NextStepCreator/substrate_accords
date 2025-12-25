#!/usr/bin/env python3
import sys
import re
from pathlib import Path

# --- Minimal YAML reader (enough for this manifest) ---
# If you prefer PyYAML, replace this with `import yaml` and yaml.safe_load.
def simple_yaml_load(text: str) -> dict:
    # Extremely small subset parser: key: value, lists with "- ", 2-level nesting.
    # Assumes manifest is well-formed and consistent with the template provided.
    data = {}
    stack = [(0, data)]
    last_key = None

    def set_value(container, key, value):
        container[key] = value

    lines = [ln.rstrip("\n") for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    for ln in lines:
        indent = len(ln) - len(ln.lstrip(" "))
        content = ln.strip()

        while stack and indent < stack[-1][0]:
            stack.pop()

        container = stack[-1][1]

        if content.startswith("- "):
            item = content[2:].strip()
            if not isinstance(container, list):
                # create list for last_key in parent
                parent = stack[-2][1]
                key = last_key
                parent[key] = []
                container = parent[key]
                stack[-1] = (stack[-1][0], container)
            if ": " in item:
                k, v = item.split(": ", 1)
                obj = {k: strip_quotes(v)}
                container.append(obj)
                stack.append((indent + 2, obj))
                last_key = k
            else:
                container.append(strip_quotes(item))
        elif ": " in content:
            k, v = content.split(": ", 1)
            v2 = strip_quotes(v)
            set_value(container, k, v2)
            last_key = k
        elif content.endswith(":"):
            k = content[:-1]
            # decide dict vs list later
            new = {}
            set_value(container, k, new)
            stack.append((indent + 2, new))
            last_key = k
        else:
            # bare value lines not supported
            pass

    return data

def strip_quotes(v: str):
    v = v.strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v

# --- Lint helpers ---
def fail(msg: str, code: int = 1):
    print(f"[LINT FAIL] {msg}")
    sys.exit(code)

def warn(msg: str):
    print(f"[LINT WARN] {msg}")

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def has_required_headings(text: str, reqs: list[str], file_label: str):
    for r in reqs:
        if r not in text:
            fail(f"{file_label}: missing required heading fragment: {r}")

def extract_protected_block(text: str, start: str, end: str) -> str:
    s = text.find(start)
    e = text.find(end)
    if s == -1 or e == -1 or e <= s:
        return ""
    return text[s + len(start):e]

def semantic_keywords_present(changelog_text: str, keywords: list[str]) -> list[str]:
    found = []
    low = changelog_text.lower()
    for kw in keywords:
        if kw.lower() in low:
            found.append(kw)
    return found

def forbid_terms_in_block(block: str, terms: list[str], label: str):
    low = block.lower()
    hits = [t for t in terms if t.lower() in low]
    if hits:
        fail(f"{label}: forbidden term(s) in II: {', '.join(hits)}")

def main():
    repo = Path(".")
    manifest_path = repo / "tools" / "manifest.yml"
    if not manifest_path.exists():
        fail("Missing tools/manifest.yml")

    manifest = simple_yaml_load(read_text(manifest_path))

    # Validate manifest basics
    versions = manifest.get("versions", {})
    rsr_version = versions.get("rsr")
    doc_version = versions.get("document")
    if not rsr_version or not doc_version:
        fail("manifest.yml must include versions.rsr and versions.document")

    constraints = manifest.get("constraints", [])
    if not constraints or not isinstance(constraints, list):
        fail("manifest.yml must include a constraints list")

    req_headings = manifest.get("required_headings", {}).get("constraint_file", [])
    if not req_headings:
        fail("manifest.yml missing required_headings.constraint_file")

    protected = manifest.get("protected_markers", {})
    start_marker = protected.get("start")
    end_marker = protected.get("end")
    if not start_marker or not end_marker:
        fail("manifest.yml missing protected_markers start/end")

    # Check each constraint file exists and is well-formed
    for c in constraints:
        if not isinstance(c, dict) or "file" not in c:
            fail("constraints entries must be dicts with 'file' keys")
        f = repo / c["file"]
        if not f.exists():
            fail(f"Missing constraint file: {c['file']}")
        text = read_text(f)

        # Required headings
        has_required_headings(text, req_headings, c["file"])

        # Protected block presence
        pb = extract_protected_block(text, start_marker, end_marker)
        if not pb.strip():
            fail(f"{c['file']}: missing or empty protected II block markers")

        # Optional: forbid normative smuggling in II
        forbid_terms_in_block(pb, ["should", "ought", "recommended", "ideally", "important"], c["file"])

    # CHANGELOG firewall
    changelog_cfg = manifest.get("changelog", {})
    changelog_path = repo / changelog_cfg.get("file", "CHANGELOG.md")
    if not changelog_path.exists():
        warn("CHANGELOG.md not found; skipping changelog checks")
    else:
        ch = read_text(changelog_path)

        keywords = changelog_cfg.get("semantic_keywords", [])
        found = semantic_keywords_present(ch, keywords)

        # Require "no semantic change" line for releases when rsr unchanged:
        # This linter can’t infer whether rsr changed between releases unless you encode history.
        # So we enforce: if document version is present and rsr is present, changelog must contain the invariant line somewhere.
        if changelog_cfg.get("require_no_semantic_change_line_if_rsr_unchanged", False):
            invariant_line = changelog_cfg.get("no_semantic_change_line", "")
            if invariant_line and invariant_line not in ch:
                fail(f"CHANGELOG.md missing required invariant line: '{invariant_line}'")

        # If semantic keywords appear in changelog, require explicit tag "RSR-BUMP:" in that release entry.
        # (This is the cheap, reliable gate without diff history.)
        if found:
            if "RSR-BUMP:" not in ch:
                fail(
                    "CHANGELOG.md contains semantic-change keywords "
                    f"({', '.join(found)}) but no 'RSR-BUMP:' tag found. "
                    "Add 'RSR-BUMP: <old> -> <new>' to the relevant release entry."
                )

    print("[LINT PASS] All checks passed.")

if __name__ == "__main__":
    main()
