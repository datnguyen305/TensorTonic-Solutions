import math

def bilinear_resize(image, new_h, new_w):
    height = len(image)
    width = len(image[0])

    output = [[0.0 for _ in range(new_w)] for _ in range(new_h)]

    scale_y = (height - 1) / (new_h - 1) if new_h > 1 else 0.0
    scale_x = (width  - 1) / (new_w - 1) if new_w > 1 else 0.0

    for i in range(new_h):
        for j in range(new_w):
            src_y = i * scale_y
            src_x = j * scale_x

            y0 = int(math.floor(src_y))
            x0 = int(math.floor(src_x))

            y1 = min(y0 + 1, height - 1)
            x1 = min(x0 + 1, width - 1)

            dy = src_y - y0
            dx = src_x - x0

            output[i][j] = (
                image[y0][x0] * (1 - dy) * (1 - dx) +
                image[y1][x0] * dy * (1 - dx) +
                image[y0][x1] * (1 - dy) * dx +
                image[y1][x1] * dy * dx
            )

    return output
