import numpy as np
import matplotlib.pyplot as plt

# Load data from gate.dat file
data = np.loadtxt('gate.dat')

# Extract time and current values
t = data[:, 0]
instantaneous_current = data[:, 1]

# Plot current vs. time
plt.plot(t, instantaneous_current)
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Instantaneous Current vs. Time')
plt.grid(True)
plt.savefig('gate1.png')
plt.show()

