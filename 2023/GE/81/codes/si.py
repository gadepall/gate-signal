import numpy as np
import matplotlib.pyplot as plt

# Define the functions f(x) and g(x)
def f(x):
    return 3 * np.cos(2*x)

def g(x):
    return (1/3) * np.sin(2*x)

# Define the convolution function
def convolution(x):
    # Define the range of integration
    a = 0
    b = 2 * np.pi
    
    # Number of intervals for numerical integration
    N = 1000
    
    # Width of each interval
    dx = (b - a) / N
    
    # Define tau values
    tau = np.linspace(a, b, N)
    
    # Compute f(tau) and g(x - tau)
    f_tau = f(tau)
    g_x_tau = g(x - tau)
    
    # Perform numerical integration using the trapezoidal rule
    integral_sum = np.sum(f_tau * g_x_tau) * dx
    
    return integral_sum

# Generate x values
x_values = np.linspace(0, 2*np.pi, 1000)

# Compute the values of f(x), g(x), and their convolution
f_values = f(x_values)
g_values = g(x_values)
convolution_values = np.array([convolution(x) for x in x_values])

# Compute convolution at x = pi/3
x_pi_over_3 = np.pi / 3
convolution_at_pi_over_3 = convolution(x_pi_over_3)


# Plot the functions
plt.figure(figsize=(10, 6))

plt.plot(x_values, f_values, label='$f(x) = 3\cos(2x)$')
plt.plot(x_values, g_values, label='$g(x) = \\frac{1}{3}\sin(2x)$')
plt.plot(x_values, convolution_values, label='$(f * g)(x)$')

plt.plot(x_pi_over_3, convolution_at_pi_over_3, 'ro', label=f'Convolution at $x = \pi/3$: {convolution_at_pi_over_3:.2f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Functions $f(x)$, $g(x)$, and their convolution $(f * g)(x)$')
plt.legend()
plt.grid(True)
plt.show()

