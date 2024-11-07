import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt("/Users/aslea/Documents/Phyton/Tarea/datos.txt")

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('ECG')
plt.show()