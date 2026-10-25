"""Prepare a local installation-only main commit from dev; never push or rewrite history."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import tempfile

from package_skill import ROOT, PUBLIC_FILES, export


def git(*args: str, env=None, data=None) -> str:
    result = subprocess.run(['git', *args], cwd=ROOT, env=env, input=data,
                            capture_output=True, check=True)
    return result.stdout.decode('utf-8').strip()


def main() -> None:
    if git('branch', '--show-current') != 'dev':
        raise SystemExit('Run from the dev branch. The active checkout is never switched.')
    if git('status', '--porcelain'):
        raise SystemExit('Commit the reviewed dev changes before preparing main.')
    if 'branch refs/heads/main' in git('worktree', 'list', '--porcelain').splitlines():
        raise SystemExit('main is checked out in another worktree; finish there before preparing a release.')
    remote = git('rev-parse', 'refs/remotes/origin/main')
    existing = subprocess.run(['git', 'rev-parse', '--verify', 'refs/heads/main'],
                              cwd=ROOT, capture_output=True)
    previous = existing.stdout.decode().strip() if existing.returncode == 0 else None
    parent = previous or remote
    if previous:
        git('merge-base', '--is-ancestor', remote, previous)
    scratch = ROOT / '.scratch'
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='release-', dir=scratch) as temp:
        base = Path(temp)
        public = base / 'repository'
        export(ROOT, public)
        release_env = os.environ.copy()
        release_env['GIT_INDEX_FILE'] = str(base / 'release.index')
        git('read-tree', '--empty', env=release_env)
        for relative in PUBLIC_FILES:
            blob = git('hash-object', '-w', '--stdin', data=(public / relative).read_bytes())
            git('update-index', '--add', '--cacheinfo', f'100644,{blob},{relative.as_posix()}', env=release_env)
        tree = git('write-tree', env=release_env)
        # Re-running an unchanged release should not add an empty release commit.
        if tree == git('rev-parse', f'{parent}^{{tree}}'):
            commit = parent
        else:
            commit = git('commit-tree', tree, '-p', parent,
                         data=b'Release installable Harness Mentor\n')
        git('update-ref', 'refs/heads/main', commit, previous or '0' * 40)
    git('branch', '--set-upstream-to=origin/main', 'main')
    print(f'Local main: {commit}')
    print('dev remains checked out. No remote was modified.')


if __name__ == '__main__':
    main()
