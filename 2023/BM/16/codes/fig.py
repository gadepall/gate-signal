"""import numpy as np
import matplotlib.pyplot as plt
def calculate_expression(omega, R, C):
 
    result = 1 / np.sqrt(1 + (omega * R * C) ** 2)
    return result

omega_values = np.linspace(-50, 50, 1000)

R = 1000  
C = 1e-4 

expression_results = calculate_expression(omega_values, R, C)
plt.figure(figsize=(8, 6))
plt.plot(omega_values, expression_results, label=r"$\frac{1}{\sqrt{1 + (\omega RC)^2}}$")
plt.xlabel(r"Angular Frequency $\omega$")
plt.ylabel("Expression Value")
plt.title("Expression vs. Angular Frequency")
plt.grid(True)
plt.legend()
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt", skiprows=0)
omega_values, result_values= data[:, 0], data[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(omega_values, result_values, label=r"$\frac{1}{\sqrt{1 + (\omega RC)^2}}$")
plt.xlabel(r"Angular Frequency $\omega$")
plt.ylabel("$|H(j\omega)|$")
plt.title("$|H(j\omega)|$ vs. Angular Frequency")
plt.grid(True)
plt.legend()
plt.show()
