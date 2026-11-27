from typing import Tuple


def reward_to_go_baseline(
    r: float, v_current: float, v_next: float, gamma: float, done: int
) -> Tuple[float, float]:
    """
    r: reward at this timestep.
    v_current: V(s_t).
    v_next: V(s_{t+1}).
    gamma: discount factor.
    done: 1 if s_t is terminal (no bootstrapped next value), else 0.

    target = r + gamma * (1 - done) * v_next
    advantage = target - v_current
    Return (target, advantage).
    """
    # TODO: zero out the bootstrapped term when done, then compute advantage
    target = r + gamma * (1 - done) * v_next
    advantage = target - v_current

    return target, advantage
    pass
