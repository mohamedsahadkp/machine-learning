

import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("../resource/data/student-mark-grade.csv")
x  = pd.DataFrame(data, columns=["gre"])
y = pd.DataFrame(data, columns=["gpa"])


plt.plot(x, y, 'ro')
plt.show()
