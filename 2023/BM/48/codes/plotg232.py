import matplotlib.pyplot as plt
import numpy as np

# Define circle parameters
center = (1, 0)
radius = 0.1

# Generate points for the circle
theta = np.linspace(0, 2*np.pi, 100)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)

# Plot the circle
plt.plot(x_circle, y_circle, label='Circle')
plt.scatter([1], [0], color='red', label='Point (1,0)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.legend()

# Save the plot
plt.savefig('plotg232.png')

# Show the plot
plt.show()
