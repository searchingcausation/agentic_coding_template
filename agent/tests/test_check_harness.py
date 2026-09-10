"""Exercise validator failure modes against isolated copies of the real harness."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_harness


class HarnessChecks(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        for name in check_harness.ROOT_FILES:
            shutil.copy2(check_harness.ROOT / name, self.root / name)
        for name in check_harness.TREES:
            shutil.copytree(check_harness.ROOT / name, self.root / name,
                            ignore=shutil.ignore_patterns("__pycache__"))

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def assert_error(self, fragment):
        errors = check_harness.validate(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_checkout(self):
        self.assertEqual(check_harness.validate(self.root), [])

    def test_missing_document_target(self):
        self.write("docs/broken.md", "[Missing](not-present.md)\n")
        self.assert_error("missing local target: not-present.md")

    def test_links_in_code_examples_are_not_live_links(self):
        self.write("docs/examples.md", "```md\n[Example](missing.md)\n```\n"
                   "`[Inline](also-missing.md)`\n"
                   "````md\n```\n[Nested](not-real.md)\n```\n````\n")
        self.assertEqual(check_harness.validate(self.root), [])

    def test_real_link_after_code_fence_is_checked(self):
        self.write("docs/fenced.md", "~~~md\n[Example](ignored.md)\n~~~\n"
                   "[Real](missing.md)\n")
        self.assert_error("missing local target: missing.md")

    def test_relative_encoded_paths_and_remote_links(self):
        self.write("docs/with space.md", "# Target\n")
        self.write("docs/links.md", "[Space](with%20space.md#heading)\n"
                   "[Angle](<with space.md>)\n"
                   "[Web](https://example.invalid/no-network)\n[Anchor](#local)\n")
        self.assertEqual(check_harness.validate(self.root), [])

    def test_links_cannot_escape_checkout(self):
        self.write("docs/escape.md", "[Outside](../../outside.md)\n")
        self.assert_error("local link leaves repository")

    def test_missing_claude_import(self):
        with (self.root / "CLAUDE.md").open("a", encoding="utf-8") as file:
            file.write("\n@does-not-exist.md\n")
        self.assert_error("missing local target: does-not-exist.md")

    def test_entrypoint_must_route_to_shared_agreement(self):
        self.write("AGENTS.md", "# Disconnected entry point\n")
        self.assert_error("AGENTS.md: must reference the shared working agreement")

    def test_adapter_drift(self):
        path = self.root / ".claude/skills/debug-fix/SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("description: ", "description: Different "), encoding="utf-8")
        self.assert_error("skill adapter metadata differs")

    def test_adapter_cannot_point_to_wrong_existing_workflow(self):
        path = self.root / ".claude/skills/debug-fix/SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("workflows/debug-fix.md", "workflows/plan-from-spec.md"),
                        encoding="utf-8")
        self.assert_error("missing matching shared workflow link")

    def test_deleted_adapter(self):
        (self.root / ".claude/skills/debug-fix/SKILL.md").unlink()
        self.assert_error("missing required skill debug-fix")

    def test_malformed_frontmatter(self):
        self.write(".claude/skills/debug-fix/SKILL.md", "---\nname: debug-fix\n")
        self.assert_error("unterminated skill frontmatter")

    def test_duplicate_frontmatter_field(self):
        self.write(".claude/skills/debug-fix/SKILL.md",
                   "---\nname: debug-fix\nname: review\ndescription: Test\n---\n")
        self.assert_error("expected unique name and description fields")

    def test_frontmatter_requires_strings_not_yaml_scalars(self):
        for scalar in ("true", "false", "null", "~", "123", "1.5"):
            with self.subTest(scalar=scalar):
                with self.assertRaises(ValueError):
                    check_harness.frontmatter(
                        f"---\nname: debug-fix\ndescription: {scalar}\n---\n"
                    )

    def test_python_and_json_syntax_errors(self):
        self.write("agent/scripts/broken.py", "def broken(:\n")
        self.write(".claude/skills/config.json", '{"broken": }\n')
        self.assert_error("broken.py")
        self.assert_error("config.json")

    def test_missing_required_file(self):
        (self.root / "ARCHITECTURE.md").unlink()
        self.assert_error("missing required file: ARCHITECTURE.md")

    def test_command_fails_for_broken_repository_from_another_directory(self):
        self.write("docs/broken.md", "[Missing](absent.md)\n")
        result = subprocess.run(
            [sys.executable, str(check_harness.ROOT / "agent/scripts/check_harness.py"),
             "--root", str(self.root)],
            cwd=self.root.parent, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("absent.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
