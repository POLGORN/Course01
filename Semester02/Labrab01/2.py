'''
Создает график какой либо функции ver.2
'''
import matplotlib.pyplot as plt
import math


def my_func(x):
    return (math.sin(x) / x)

# plt.xkcd()

styles = plt.style.available
plt.style.use(styles[3])

x = 5
legend = f'y = sin({x}) / {x}'
left = -100; right = 100; step = 0.5

data_x = []; data_y = []
pos_x = left
while pos_x <= right:
    try:
        pos_y = my_func(pos_x)
        data_x.append(pos_x) 
        data_y.append(pos_y)
    except:
        pass
    pos_x += step

plt.plot(data_x, data_y, linewidth=4, color='#000000')

plt.legend([legend])
plt.grid(True)
plt.axhline(linewidth=3, color='#00FFFF')
plt.axvline(linewidth=3, color='#00FFFF')

plt.show()
