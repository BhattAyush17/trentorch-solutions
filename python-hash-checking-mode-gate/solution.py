def check_hash_mode(requirements: list[dict]) -> list[str]:
    """
    Validate pinned and hashed requirements when hash-checking mode is active.
    """
    # Hash mode is active if at least one requirement has hashes.
    hash_mode_active = any(req["hashes"] for req in requirements)

    if not hash_mode_active:
        return []

    errors = []

    # Sort by requirement name.
    for req in sorted(requirements, key=lambda r: r["name"]):
        name = req["name"]
        spec = req["spec"]
        hashes = req["hashes"]

        # Pinned means starts with == and contains no wildcard.
        if not spec.startswith("==") or "*" in spec:
            errors.append(f"{name}: not pinned")

        # Hash list must be non-empty.
        if not hashes:
            errors.append(f"{name}: missing hash")

    return errors
