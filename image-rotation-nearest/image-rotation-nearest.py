import math

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    H = len(image)
    W = len(image[0])

    # Center of the image
    cy = (H-1)/2
    cx = (W-1)/2

    output = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            dy = i - cy 
            dx = j - cx

            theta = math.radians(angle_degrees)
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)

            src_y = cy + dy*cos_t + dx*sin_t
            src_x = cx - dy*sin_t + dx*cos_t
            src_y = int(round(src_y))
            src_x = int(round(src_x))
            if src_x <= W and src_y <= H:
                output[i][j] = image[src_y][src_x]
    return output