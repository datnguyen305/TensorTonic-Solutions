import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    x = np.asarray(p)
    target = np.asarray(y)

    x = x.flatten()
    target = target.flatten()
    dice = (2 * np.sum(x * target) + eps) / (np.sum(x) + np.sum(target) + eps)
    dice_loss = 1 - dice
    return dice_loss

