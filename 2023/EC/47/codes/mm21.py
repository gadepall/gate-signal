import numpy as np
import matplotlib.pyplot as plt

# Read phase values from file
phase_X_k = np.loadtxt('mm21.dat')

# Set phase to NaN where undefined (e.g., k=5,6,7)
phase_X_k[5:8] = np.nan

# Plot the phase of X(k)
plt.stem(range(len(phase_X_k)), phase_X_k)
plt.xlabel('$k$')
plt.ylabel('$Phase$')
plt.grid(True)
plt.savefig('mm21.png')
plt.show()

