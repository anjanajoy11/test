import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4,5,7,6])
ypoints = np.array([1,2,3,4])

plt.plot(xpoints, ypoints, marker = 'o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.grid()
plt.show()
