def color_to_grayscale(image):
    H = len(image)
    W = len(image[0])
    
    result = []
    
    for i in range(H):
        row = []
        for j in range(W):
            pixel = image[i][j]
            gray = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
            row.append(float(gray))
        result.append(row)
    
    return result