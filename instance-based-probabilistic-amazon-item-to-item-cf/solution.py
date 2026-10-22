import math
from collections import defaultdict


def recommend(
    num_users: int,
    num_items: int,
    purchases: list[tuple[int, int]],
    cart: list[int],
    k: int,
) -> list[tuple[int, float]]:
    """
    "Customers who bought this also bought...": the top k items to recommend
    for a shopping cart, by item-to-item collaborative filtering.
    """
    # Each user counts once per item.
    user_items = defaultdict(set)

    for user, item in purchases:
        user_items[user].add(item)

    # Item -> set of users who purchased it.
    item_users = defaultdict(set)

    for user, items in user_items.items():
        for item in items:
            item_users[item].add(user)

    # Cart is a set: duplicate cart items count only once.
    cart_set = set(cart)

    # Count how many cart-item purchasers overlap with each candidate item.
    common_counts = defaultdict(int)

    for cart_item in cart_set:
        users = item_users.get(cart_item, set())

        for user in users:
            for item in user_items[user]:
                if item not in cart_set:
                    common_counts[item] += 1

    scores = []

    for item, common in common_counts.items():
        users_cart_item = item_users.get(item, set())
        item_count = len(users_cart_item)

        if item_count == 0 or common == 0:
            continue

        score = 0.0

        # We need the contribution from each cart item separately.
        for cart_item in cart_set:
            cart_users = item_users.get(cart_item, set())
            overlap = len(cart_users & users_cart_item)

            if overlap:
                score += overlap / (
                    math.sqrt(len(cart_users)) * math.sqrt(item_count)
                )

        if score > 0:
            scores.append((item, score))

    # Scores tied to 9 decimal places; smaller item ID wins.
    scores.sort(key=lambda pair: (-round(pair[1], 9), pair[0]))

    return scores[:k]
