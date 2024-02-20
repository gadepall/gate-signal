import numpy as np
import matplotlib.pyplot as plt

# Assuming data.txt has three columns: t, x_o_t, x_t
data = np.loadtxt("data.txt", skiprows=0)
t_values, x_o_t_values, x_t_values = data[:, 0], data[:, 1], data[:, 2]

# Plot the line plots
plt.plot(t_values, x_o_t_values, 'r-', label='without damping')
plt.plot(t_values, x_t_values, 'b-', label='with damping')

# Set labels and legend
plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()
