"""Release boundary tests with synthetic files, without real context or credentials."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('package_skill', Path(__file__).resolve().parents[1] / 'scripts/package_skill.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class ReleaseBoundaryTests(unittest.TestCase):
    def fixture(self, root):
        for relative in package.PUBLIC_FILES:
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f'synthetic {relative}', encoding='utf-8')

    def test_only_required_installation_files_are_exported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'dev'
            root.mkdir()
            self.fixture(root)
            for relative in ['DECISIONS.md', 'evals/results/raw/test.txt', '.qoder/skills/company-harness/SKILL.md', '.qoder/skills/harness-mentor/references/unapproved.md']:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('development-only synthetic marker')
            out = Path(temp) / 'public'
            package.export(root, out)
            self.assertEqual({p.relative_to(out) for p in out.rglob('*') if p.is_file()}, set(package.PUBLIC_FILES))

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root, out = Path(temp) / 'dev', Path(temp) / 'public'
            root.mkdir()
            self.fixture(root)
            out.mkdir()
            marker = out / 'keep.txt'
            marker.write_text('keep')
            with self.assertRaises(ValueError):
                package.export(root, out)
            self.assertEqual(marker.read_text(), 'keep')

    def test_incomplete_skill_does_not_create_partial_release(self):
        with tempfile.TemporaryDirectory() as temp:
            root, out = Path(temp) / 'dev', Path(temp) / 'public'
            root.mkdir()
            self.fixture(root)
            (root / package.SKILL / 'references/bestandsaufnahme.md').unlink()
            with self.assertRaises(ValueError):
                package.export(root, out)
            self.assertFalse(out.exists())


if __name__ == '__main__':
    unittest.main()
