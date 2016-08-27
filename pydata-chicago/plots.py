import numpy as np
import matplotlib as mpl
mpl.use('Qt4Agg')
import matplotlib.pyplot as plt

#from data import fizz_buzz_encode

def fizz_buzz_encode(i):
    """encodes the desired fizz-buzz output as a one-hot array of length 4:
    [number, "fizz", "buzz", "fizzbuzz"]"""
    if   i % 15 == 0: return np.array([0, 0, 0, 1])
    elif i % 5  == 0: return np.array([0, 0, 1, 0])
    elif i % 3  == 0: return np.array([0, 1, 0, 0])
    else:             return np.array([1, 0, 0, 0])

d = ['1','buzz','fizz','4','buzz','fizz','7','8','fizz','buzz','11','fizz','13',
 '14','fizzbuzz','16','buzz','fizz','buzz','buzz','buzz','22','23','fizz',
 'fizz','26','fizz','28','29','fizzbuzz','31','32','fizz','buzz','buzz',
 'fizz','37','buzz','fizz','buzz','41','fizz','43','44','fizzbuzz','46',
 '47','fizz','buzz','buzz','fizz','52','53','fizz','buzz','56','fizz','58',
 '59','fizzbuzz','61','62','fizz','64','buzz','fizz','67','68','69','buzz',
 '71','fizz','73','74','fizzbuzz','76','77','fizz','79','buzz','buzz','82',
 '83','84','buzz','86','87','88','89','fizzbuzz','91','92','93','94','buzz',
 'fizz','97','fizz','fizz','buzz']

def make_array(data):
    """
    turn a list of fuzzbuzz outputs into a 2-D array for plotting
    """
    black = [0.0, 0.0, 0.0]
    red = [1.0, 0.0, 0.0]
    chicago_blue = [179/255,221/255,242/255]

    lookup = { "fizz" : 1, "buzz" : 2, "fizzbuzz" : 3 }
    n = len(data)
    grid = np.full((4, n, 3), 1.0)
    for i, output in enumerate(data):
        actual = np.argmax(fizz_buzz_encode(i+1))
        predicted = lookup.get(output, 0)

        # correct predictions
        grid[predicted][i] = black

        if actual != predicted:
            grid[actual][i]    = chicago_blue
            grid[predicted][i] = red

    return grid

def plot(data, fn=None):
    grid = make_array(data)
    plt.axis('off')
    plt.imshow(grid, interpolation='none')
    if fn:
        plt.savefig(fn, bbox_inches='tight')
    else:
        plt.show()

from PIL import Image
def plot2(output, fn, dim):
    data = make_array(output)
    data = np.uint8(data * 255)
    Image.fromarray(data).convert('RGB').resize(dim).save(fn)


def ct(data):
    """
    create a crosstab from the fizz buzz outputs
    """
    lookup = { "fizz" : 1, "buzz" : 2, "fizzbuzz" : 3 }
    grid = [[0 for _ in range(4)] for _ in range(4)]
    for i, output in enumerate(data):
        actual = np.argmax(fizz_buzz_encode(i+1))
        predicted = lookup.get(output, 0)
        grid[predicted][actual] += 1
    return grid
