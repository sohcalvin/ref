import numpy as np
from scipy.misc import imsave,imshow
from scipy.ndimage import median_filter
import matplotlib.pyplot as pl

def genImageRandom() :
    # random_array = np.random.random_sample((512,512))
    random_array = np.random.uniform(0,1,(512,512))
    # random_array[random_array < 0.999] *= 0.25
    random_array[random_array < 0.999] *= 0
    imsave('white_specs_before.png', random_array)
    filtered_array = median_filter(random_array, size=3)
    imsave('white_specs_after.png', filtered_array)

# genImageRandom()

def genPoisson() :
    random_array = np.random.poisson(1,(512,512))
    random_array = random_array/8
    print(random_array)
    imsave('poisson.png', random_array)
    imshow( random_array)

genPoisson()

