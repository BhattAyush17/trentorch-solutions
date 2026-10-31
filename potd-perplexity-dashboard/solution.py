import math


def perplexity_dashboard(losses: list[float]) -> tuple[float, float]:
    """
    losses: a list of N per-token negative log-likelihood values.

    H = mean(losses)
    PPL = e^H

    Return (mean_loss, perplexity). Exponentiate the MEAN, never the sum.
    """
    # TODO: average first, then exponentiate once.
    mean_loss = sum(losses)/len(losses)
    perplexity = math.exp(mean_loss)

    return float(mean_loss), float(perplexity)
    pass
