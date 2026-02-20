import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    stride = image_size / feature_size
    anchors = []

    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            for s in scales:
                for ar in aspect_ratios:
                    w = s * np.sqrt(ar)
                    h = s / np.sqrt(ar)

                    x1 = cx - w / 2
                    y1 = cy - h / 2
                    x2 = cx + w / 2
                    y2 = cy + h / 2

                    anchors.append([x1, y1, x2, y2])

    return anchors