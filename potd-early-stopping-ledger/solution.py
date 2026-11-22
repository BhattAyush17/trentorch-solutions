from typing import List, Tuple


def early_stopping_ledger(losses: List[float], patience: int) -> Tuple[int, float]:
    """
    losses: validation losses in epoch order, length n.
    patience: number of consecutive non-improving epochs that triggers a stop.

    Track the best loss seen so far (starts at +infinity) and a
    non-improving counter. An epoch improves iff its loss is strictly less
    than the best so far: reset the counter and update best on improvement,
    otherwise increment the counter. Stop at the first epoch where the
    counter reaches patience. If that never happens, stop after the final
    epoch. Return (1-based stop epoch, best loss observed through that
    epoch).
    """
    # TODO: walk losses, track best + non-improving streak, stop on patience.
    best_loss = float("inf")
    non_improving = 0
    stop_epoch = 0

    for epoch, loss in enumerate(losses, start=1):
        stop_epoch = epoch

        if loss < best_loss:
            best_loss = loss
            non_improving = 0
        else:
            non_improving += 1

        if non_improving >= patience:
            break

    return stop_epoch, best_loss
    pass
