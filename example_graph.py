import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10, 0.01)
y1 = np.sqrt(x)
y2 = -1 * np.sqrt(x)
fig = plt.figure()

ax = fig.add_subplot(1,1,1)
plt.plot(x, y1, 'red')
plt.plot(x, y2, 'blue')
plt.axhline(y = 0, color = 'black', linestyle = '-', linewidth = 0.5)
plt.axvline(x = 0, color = 'black', linestyle = '-', linewidth = 0.5)
plt.xlim([-5, 10])

plt.show()



