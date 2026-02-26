import numpy as np
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    T = len(actual_tokens)
    prob_distributions = np.asarray(prob_distributions)
    actual_tokens = np.asarray(actual_tokens)
    score = prob_distributions[np.arange(T), actual_tokens]
    H = -np.mean(np.log(score))
    PP = np.exp(H)
    return PP 