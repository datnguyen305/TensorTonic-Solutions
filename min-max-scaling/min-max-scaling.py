def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    H = len(data)
    num_features =  len(data[0])

    for i in range(num_features):
        min_val = float('inf')
        max_val = float('-inf')
        for j in range(H):
            if data[j][i] < min_val:
                min_val = data[j][i]
            if data[j][i] > max_val:
                max_val = data[j][i]
        for j in range(H):
            if max_val - min_val != 0: 
                data[j][i] = (data[j][i] - min_val) / (max_val-min_val)
            else:
                data[j][i] = 0.0
    return data
            