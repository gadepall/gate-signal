import numpy as np
import matplotlib.pyplot as plt

# Read phase values from file
phase_X_k = np.loadtxt('mm11.dat')

# Plot the phase of X(k)
plt.stem(range(len(phase_X_k)), phase_X_k)
plt.xlabel('$k$')
plt.ylabel('$Phase$')
plt.grid(True)
plt.savefig('mm11.png')
plt.show()

