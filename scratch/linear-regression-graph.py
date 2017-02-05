# Plot Graph 

""" Dependencies
   sudo pip install matplotlib
   sudo apt-get install python-tk """

import matplotlib.pyplot as plt
import pandas as pd

# Read traning data
data = pd.read_csv("../resource/data/student-study-mark.csv")
x = pd.DataFrame(data, columns=["number_of_hour_study"])
y = pd.DataFrame(data, columns=["mark_secured"])

plt.plot(x, y, 'ro')

plt.show()