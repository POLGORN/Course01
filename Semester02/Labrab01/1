import matplotlib.pyplot as plt
import numpy as np


styles = plt.style.available
plt.style.use(styles[3])

x = np.linspace(-5, 5, 100)
y = abs(x)

fig, ax = plt.subplots()

ax.plot(x, y, color = '#000000', lw = 3)
ax.vlines(0, y.min(), y.max(), color = '#00FFFF', lw = 2)
ax.hlines(0, x.min(), x.max(), color = '#00FFFF', lw = 2)

fig.set_figwidth(8); fig.set_figheight(8)

plt.show()
