import numpy as np
import matplotlib.pyplot as plt

# Function to calculate x(t) based on the given Fourier transform
def x_t(t, w_0):
    return np.sinc(w_0 * t / np.pi)

# Values for time (t) and the cutoff frequency (w_0)
t_values = np.linspace(-10, 10, 1000)
w_0 = 2 * np.pi * 1  # You can adjust the value of w_0 as needed

# Calculate x(t)
x_values = x_t(t_values, w_0)

# Plotting
plt.plot(t_values, x_values, label=r'$x(t) = \frac{\sin(\omega_0 t)}{\pi t}$')
plt.title('Plot of $x(t)$')
plt.xlabel('Time $t$')
plt.ylabel('$x(t)$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.savefig('figs/main.png')
plt.show()
