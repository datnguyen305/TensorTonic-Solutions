def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    total_scores=[]
    for avg_rate, num_votes in items:
        scores = (num_votes/(num_votes + min_votes))*avg_rate+(min_votes/(num_votes+min_votes))*global_mean
        total_scores.append(scores)

    return total_scores