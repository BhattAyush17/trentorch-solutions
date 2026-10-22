# Is the Lockfile Stale?

Intermediate | python-packaging | reproducible-environments | lockfile | uv

Write `stale_packages(declared, locked)`, which reports which declared dependencies the lockfile no longer satisfies, the check behind a `--locked` install in CI.
