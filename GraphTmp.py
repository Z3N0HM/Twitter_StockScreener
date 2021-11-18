import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i=None):
    graph_data = open('StocksParsed.txt'. 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(':')
            xs.append(str(x))
            ys.append(int(y))
    ax1.clear()
    ax1.plot(xs, ys)