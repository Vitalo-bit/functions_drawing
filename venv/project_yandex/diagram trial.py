import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10)
y = np.random.randint(1, 20, size = 9)

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()