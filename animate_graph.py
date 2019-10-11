import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 10, 100)
y = np.sin(x)


fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')

for n in range(len(x)):
    line.set_data(x[:n], y[:n])
    ax.axis([0, 10, 0, 1])
    fig.canvas.draw()
    fig.savefig('Frame%03d.png' %n)
	

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 1])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=25, blit=False)
ani.save('test.gif')
plt.show()

