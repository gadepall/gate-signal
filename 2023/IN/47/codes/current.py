import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
I_0 = 1  # Initial current
R_over_L = 1e7  # R/L

# Define the time range
t = np.linspace(0, 1e-6, 1000)  # Time from 0 to 1e-6 seconds

# Calculate the current values
I = I_0 - (4/5) * I_0 * np.exp(-10**7 * t)

# Plot the graph
plt.plot(t, I, label=r'$I(t) = I_0 - \frac{4}{5}I_0 e^{-10^{7}t}$')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current vs. Time')

# Find the index of t closest to 0.43 microseconds
idx = np.abs(t - 0.43e-6).argmin()

# Draw a vertical line at t=0.43 microseconds
plt.axvline(x=0.43e-6, color='red', linestyle='--', ymax=I[idx]/plt.ylim()[1])

# Draw a horizontal line at the current value at t=0.43 microseconds
plt.axhline(y=I[idx], color='red', linestyle='--', xmax=0.43e-6/plt.xlim()[1])

plt.legend()
plt.grid(True)
plt.show()
