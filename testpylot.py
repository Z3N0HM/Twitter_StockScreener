import matplotlib.pyplot as plt

from NewGraph import *


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ["Code", "Python", "Snake"]
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()