#!/usr/bin/env python3
"""Offline checks for this template's documented, intentionally small file contract."""

import argparse
import ast
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
TREES = ("agent", "docs", ".agents/skills", ".claude/skills", ".github")
ROOT_FILES = ("README.md", "AGENTS.md", "CLAUDE.md", "ARCHITECTURE.md", "Makefile")
REQUIRED = ROOT_FILES + (
    "agent/README.md",
    "docs/README.md",
    "docs/product-specs/template.md",
    "docs/design-decisions/template.md",
    "docs/exec-plans/template.md",
    ".github/workflows/check.yml",
)
SKILLS = ("plan-from-spec", "debug-fix", "independent-review")
SKIP_DIRS = {"__pycache__", ".git", ".venv", "venv", "node_modules", "build", "dist"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"\n]*\")?\s*\)")


def files_in_scope(root):
    """Restrict scanning to maintained harness files, without following symlink trees."""
    files = {root / name for name in ROOT_FILES if (root / name).is_file()}
    for tree in TREES:
        for directory, children, names in os.walk(root / tree):
            children[:] = sorted(name for name in children if name not in SKIP_DIRS)
            files.update(Path(directory) / name for name in names)
    return sorted(files)


def prose_lines(text):
    """Yield lines outside fenced blocks, with inline code removed."""
    marker = None
    length = 0
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            chars, tail = fence.groups()
            if marker is None:
                marker, length = chars[0], len(chars)
            elif chars[0] == marker and len(chars) >= length and not tail.strip():
                marker = None
            continue
        if marker is None:
            yield number, re.sub(r"(`+).*?\1", "", line)


def local_links(text, imports=False):
    for number, line in prose_lines(text):
        for match in LINK.finditer(line):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if not parsed.scheme and not parsed.netloc and parsed.path:
                yield number, unquote(parsed.path)
        if imports:
            match = re.fullmatch(r"\s*@([^\s]+)\s*", line)
            if match:
                yield number, match.group(1)


def frontmatter(text):
    """Read name/description-only, single-line YAML strings starting with a letter.

    Other YAML forms are rejected instead of guessed; extend this contract or
    adopt a YAML parser when richer native skill metadata is needed.
    """
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("missing or unterminated skill frontmatter")
    metadata = {}
    for line in lines[1:lines.index("---", 1)]:
        key, separator, value = line.partition(": ")
        if not separator or key not in {"name", "description"} or key in metadata:
            raise ValueError("expected unique name and description fields")
        if (not re.match(r"^[A-Za-z]", value) or value != value.strip()
                or value.lower() in {"true", "false", "null", "yes", "no", "on", "off"}
                or ": " in value or " #" in value):
            raise ValueError("skill metadata must use plain single-line YAML strings")
        metadata[key] = value
    if set(metadata) != {"name", "description"}:
        raise ValueError("skill requires name and description")
    name = metadata["name"]
    if len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("invalid skill name")
    description = metadata["description"]
    if len(description) > 1024 or "<" in description or ">" in description:
        raise ValueError("invalid skill description")
    return metadata


def check_skills(root, errors):
    catalogs = []
    for tool in (".agents", ".claude"):
        folder = root / tool / "skills"
        paths = sorted(folder.glob("*/SKILL.md"))
        catalog = {}
        for path in paths:
            label = path.relative_to(root)
            try:
                text = path.read_text(encoding="utf-8")
                metadata = frontmatter(text)
                name = metadata["name"]
                if name != path.parent.name:
                    errors.append(f"{label}: skill name must match directory")
                if name in catalog:
                    errors.append(f"{label}: duplicate skill name {name}")
                expected = (root / "agent/workflows" / f"{name}.md").resolve()
                targets = [(path.parent / target).resolve() for _, target in local_links(text)]
                if expected not in targets or not expected.is_file():
                    errors.append(f"{label}: missing matching shared workflow link")
                catalog[name] = metadata
            except (OSError, UnicodeError, ValueError) as error:
                errors.append(f"{label}: {error}")
        for name in SKILLS:
            if name not in catalog:
                errors.append(f"{tool}/skills: missing required skill {name}")
        catalogs.append(catalog)
    if catalogs[0] != catalogs[1]:
        errors.append("skill adapter metadata differs between Codex and Claude Code")


def validate(root):
    root = root.resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")
    for name in ("docs/exec-plans/active", "docs/exec-plans/completed"):
        if not (root / name).is_dir():
            errors.append(f"missing task directory: {name}")

    for path in files_in_scope(root):
        if path.suffix not in {".md", ".py", ".json"}:
            continue
        label = path.relative_to(root)
        if not path.resolve().is_relative_to(root):
            errors.append(f"{label}: harness file points outside repository")
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix == ".py":
                ast.parse(text, filename=str(label), feature_version=(3, 11))
            elif path.suffix == ".json":
                json.loads(text)
            else:
                for number, target in local_links(text, imports=path.name == "CLAUDE.md"):
                    destination = (path.parent / target).resolve()
                    if not destination.is_relative_to(root):
                        errors.append(f"{label}:{number}: local link leaves repository: {target}")
                    elif not destination.exists():
                        errors.append(f"{label}:{number}: missing local target: {target}")
        except (OSError, UnicodeError, ValueError, SyntaxError) as error:
            errors.append(f"{label}: {error}")

    shared = (root / "agent/README.md").resolve()
    for name in ("AGENTS.md", "CLAUDE.md"):
        path = root / name
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
                targets = {(path.parent / target).resolve()
                           for _, target in local_links(text, imports=True)}
                if shared not in targets:
                    errors.append(f"{name}: must reference the shared working agreement")
            except (OSError, UnicodeError, ValueError):
                pass  # The file scan already reports unreadable/invalid content.
    check_skills(root, errors)
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository to validate")
    args = parser.parse_args(argv)
    if sys.version_info < (3, 11):
        print("ERROR: Python 3.11+ is required.", file=sys.stderr)
        return 2
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Harness checks passed (structure, links, skill parity, Python/JSON syntax).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
