import numpy as np
import matplotlib.pyplot as plt

# Generate values for t
t = np.linspace(0, 0.002, 1000)  # Time from 0 to 0.002 seconds

# Calculate Vr and Vs
Vr = 100 * np.cos(10**4 * t)
Vs = 100 * np.cos(10**4 * t)

# Plot Vr with a solid blue line
plt.plot(t, Vr, label='Vr', color='blue', linestyle='-')

# Plot Vs with a dashed red line
plt.plot(t, Vs, label='Vs', color='red', linestyle='--')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()

# Display the plot
plt.show()
