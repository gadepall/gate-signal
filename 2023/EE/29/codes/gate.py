import numpy as np
import matplotlib.pyplot as plt

# Define the voltage function
def voltage_function(t):
    return np.exp(-200 * t) * (
        -0.06 * ((2300 * np.sin(400 * np.sqrt(6) * t) + 400 * np.sqrt(6) * np.cos(400 * np.sqrt(6) * t)) / np.sqrt(6))
        + 32 * ((2 * np.sqrt(6) * np.cos(400 * np.sqrt(6) * t) - np.sin(400 * np.sqrt(6) * t)) / (2 * np.sqrt(6)))
        + 10**5 * (np.sin(400 * np.sqrt(6) * t) / (400 * np.sqrt(6)))
    )

# Calculate voltage at t=0+
voltage_at_zero_plus = voltage_function(0)

# Generate values for t
t_values = np.linspace(0, 0.01, 1000)  # Adjust the range and number of points as needed

# Calculate corresponding voltage values
voltage_values = voltage_function(t_values)

# Plot the voltage function
plt.plot(t_values, voltage_values, label='Voltage Function')

# Highlight voltage at t=0+
plt.scatter([0], [voltage_at_zero_plus], color='red', label=f'Voltage at $t=0^+$: {voltage_at_zero_plus:.2f}')

# Set labels and title
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.title('Voltage as a function of time')

plt.grid(True)
plt.legend()
plt.savefig('c.png')
# Show the plot
plt.show()
