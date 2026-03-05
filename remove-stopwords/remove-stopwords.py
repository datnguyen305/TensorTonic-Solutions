def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)
    result = []
    for value in tokens:
        if value not in stopwords:
            result.append(value)
    
    return result
        