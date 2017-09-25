import numpy as np
import cv2
import os

def noise(noise_type, image):
    if noise_type=='gauss':
        row, col, ch=image.shape
        mean=0
        # var = 1, sigma = var**0.5
        gauss=np.random.normal(mean, 1, (row, col, ch))
        gauss= gauss.reshape(row, col, ch)
        noisy=image+gauss
        return noisy
    elif noise_type=='s&p':
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        # Salt mode
        num_salt = np.ceil(amount*image.size*s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1
        # Peper mode
        num_pepper = np.ceil(amount*image.size*(1. - s_vs_p))
        coords=[np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out
    elif noisy_type=='poisson':
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy=np.random.poisson(image*vals)/float(vals)
        return noisy
    elif noise_type=='speckle':
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image*gauss
        return noisy
