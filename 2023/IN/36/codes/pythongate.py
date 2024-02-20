import numpy as np
import matplotlib.pyplot as plt

# Define the input signals x(t) and y(t)
def x(t):
    return np.cos(7*np.pi*t/4)

def y(t):
    return 0.5 * np.cos(7*np.pi*t/4)

# Define the time range
t = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Plot x(t) and y(t)
plt.figure(figsize=(10, 6))
plt.plot(t, x(t), label='$x(t) = \cos(\\frac{7\pi t}{4})$')
plt.plot(t, y(t), label='$y(t) = 0.5\cos(\\frac{7\pi t}{4})$')
plt.title('Input and Output Signals')
plt.xlabel('Time $t$')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()



