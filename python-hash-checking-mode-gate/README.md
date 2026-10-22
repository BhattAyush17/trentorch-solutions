# The All-or-Nothing Hash-Checking Gate

Intermediate | python-packaging | reproducible-environments | hashing | validation

Write `check_hash_mode(requirements)`, which models pip's hash-checking mode: if any requirement carries a hash the whole file is held to the strict rules, and the function returns every violation.
