"""Exercise branch separation in a disposable local Git repository, without any remote access."""
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('prepare_release', SCRIPTS / 'prepare_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseBranchTests(unittest.TestCase):
    def test_main_has_only_installation_files_and_keeps_public_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.STDOUT).decode().strip()
            git('init', '-b', 'dev')
            git('config', 'user.name', 'Synthetic release test')
            git('config', 'user.email', 'test@example.invalid')
            for relative in release.PUBLIC_FILES:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('synthetic skill source')
            (root / 'DECISIONS.md').write_text('synthetic old public planning')
            git('add', '.')
            git('commit', '-m', 'Synthetic existing public history')
            public_parent = git('rev-parse', 'HEAD')
            git('update-ref', 'refs/remotes/origin/main', public_parent)
            # A local-only fake remote enables normal tracking metadata, never a network call.
            git('config', 'remote.origin.url', str(root / 'unused-remote'))
            git('config', 'remote.origin.fetch', '+refs/heads/*:refs/remotes/origin/*')
            (root / 'README.md').write_text('synthetic new user instructions')
            (root / 'evals').mkdir()
            (root / 'evals/cases.json').write_text('synthetic internal cases')
            git('add', '.')
            git('commit', '-m', 'Synthetic development work')
            dev_head = git('rev-parse', 'HEAD')
            with patch.object(release, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()):
                release.main()
            self.assertEqual(git('branch', '--show-current'), 'dev')
            self.assertEqual(git('rev-parse', 'HEAD'), dev_head)
            self.assertEqual(git('rev-parse', 'main^'), public_parent)
            self.assertEqual(set(git('ls-tree', '-r', '--name-only', 'main').splitlines()), {p.as_posix() for p in release.PUBLIC_FILES})
            # Ignore the release script's disposable workspace as the real dev repository does.
            self.assertEqual(git('diff', '--name-only'), '')
            self.assertEqual(git('diff', '--cached', '--name-only'), '')
            first_release = git('rev-parse', 'main')
            (root / '.gitignore').write_text('.scratch/\n')
            git('add', '.gitignore')
            git('commit', '-m', 'Synthetic scratch exclusion')
            with patch.object(release, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()):
                release.main()
            self.assertEqual(git('rev-parse', 'main'), first_release)


if __name__ == '__main__':
    unittest.main()
