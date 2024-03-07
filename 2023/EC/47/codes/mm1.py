import numpy as np
import matplotlib.pyplot as plt

# Read amplitude values from file
data = np.loadtxt('mm1.dat')
k_values = data[:, 0]
amplitude_X_values = data[:, 1]

# Plot the amplitude of X[k]
plt.stem(k_values, amplitude_X_values)
plt.xlabel('$k$')
plt.ylabel('$|X(k)|$')
plt.grid(True)
plt.savefig('mm1.png')
plt.show()

