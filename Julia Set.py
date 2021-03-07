 # -*- coding: utf-8 -*-
"""
JUILA SET FRACTAL

By: it's literally monique
"""

# import necessary libraries 
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
rows = 10000
cols = 10000
iterations = 150

def julia(c, z):
    global iterations
    count = 0
    for i in range(iterations):
        z = (z * z) + c
        count += 1
        if (abs(z) > 4):
            break
    return count

def julia_set(x, y):
    global iterations
    output = np.zeros((len(x),len(y)))
    
    # a lot of different patterns to try
    # check out this website: http://paulbourke.net/fractals/juliaset/
    c = complex(-0.4, -0.59)
    for i in range(len(x)):
        for j in range(len(y)):
            z = complex(x[i], y[j])
            count = julia(c, z)
            output[i, j] = count
    return output
    
x = np.linspace(-2, 2, rows)
y = np.linspace(-2, 2, cols)


j = julia_set(x, y)

# show the set (best colors: binary, hot, bone, magma)
plt.imshow(j.T, cmap='magma')
plt.axis("off")
plt.savefig('julia_set.png', dpi=300, bbox_inches='tight')
plt.show()
