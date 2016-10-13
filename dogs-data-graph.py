# Plot Graph 

""" Dependencies
   sudo pip install matplotlib
   sudo apt-get install python-tk """

import numpy as np
import matplotlib.pyplot as plt

gray = 500
labs = 500

#print np.random.randn(gray)
gray_height = 28 + 4 * np.random.randn(gray)
labs_height = 24 + 4 * np.random.randn(labs)

plt.hist([gray_height,labs_height], stacked = True, color=['g','b'])
plt.show()