def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    result = []
    for x in values:
        result.append([x**p for p in range(degree + 1)])
    return result 