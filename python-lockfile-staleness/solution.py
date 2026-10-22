def _version_key(version: str) -> tuple:
    parts = tuple(int(part) for part in version.split("."))

    # Remove trailing zero components.
    parts = list(parts)
    while parts and parts[-1] == 0:
        parts.pop()

    return tuple(parts)


def stale_packages(declared: dict[str, str], locked: dict[str, str]) -> list[str]:
    """
    Return declared packages whose locked version does not satisfy
    the declared minimum version.
    """
    stale = []

    for name, minimum in declared.items():
        if name not in locked:
            stale.append(name)
            continue

        if _version_key(locked[name]) < _version_key(minimum):
            stale.append(name)

    return sorted(stale)
