import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(2*x) + np.exp(-x)

# Generate x values using linspace
x_values = np.arange(0, 3,0.0001)  # Adjust the range as needed

# Generate y values
y_values = f(x_values)

# Plot the function
plt.plot(x_values,y_values,label= 'y(x)')
plt.plot(1,f(1),marker='o',markerfacecolor='red',label='y(1)')
# Label axes and add legend
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.legend()
# Show the plot
plt.show()

