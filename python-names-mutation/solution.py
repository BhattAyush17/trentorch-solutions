def mutate_list(lst: list) -> None:
    """
    Mutate `lst` in place by appending the value 4 to it.
    """
    lst.append(4)


def reassign_list(lst: list) -> list:
    """
    Create a brand-new list without modifying the original.
    """
    return [9, 9, 9]


def observe_through_alias(original: list) -> dict:
    """
    Demonstrate aliasing versus reassignment.
    """
    alias = original

    original.append(100)
    alias_after_mutation = alias.copy()

    original = [0, 0, 0]
    alias_after_reassignment = alias.copy()

    return {
        "alias_after_mutation": alias_after_mutation,
        "alias_after_reassignment": alias_after_reassignment,
        "original_final": original
    }


def is_mutable_type(value) -> bool:
    """
    Return True for common mutable types and custom instances.
    """
    return isinstance(value, (list, dict, set)) or (
        hasattr(value, "__dict__")
        and not isinstance(value, type)
    )


def tuple_inner_mutation_check(t: tuple) -> dict:
    """
    Mutate the list contained inside the tuple.
    """
    tuple_id_before = id(t)

    t[0].append(100)

    tuple_id_after = id(t)

    return {
        "tuple_id_before": tuple_id_before,
        "tuple_id_after": tuple_id_after,
        "inner_list_after": t[0]
    }
