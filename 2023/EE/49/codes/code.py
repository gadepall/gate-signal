import numpy as np
import matplotlib.pyplot as plt

# Given signal parameters
N = 48
n_values = np.arange(N)
x_n = 1 + 3 * np.sin((15 * np.pi / 8) * n_values + (3 * np.pi / 4)) - 5 * np.sin((np.pi / 3) * n_values - (np.pi / 4))

# DFT coefficients (from previous calculation)
X_k = np.array([48.0000 + 0.0000j, 0.0000 - 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ,50.9117 - 50.9117j, -0.0000 + 0.0000j, 0.0000 - 0.0000j
                ])

# Compute magnitude and phase of X[k]
magnitude_X_k = np.abs(X_k)
phase_X_k = np.angle(X_k)

# Plot x[n]
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(n_values, x_n)
plt.title("Signal x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")

# Plot magnitude of X[k]
plt.subplot(3, 1, 2)
plt.stem(np.arange(N), magnitude_X_k)
plt.title("Magnitude of X[k]")
plt.xlabel("k")
plt.ylabel("|X[k]|")

# Plot phase of X[k]
plt.subplot(3, 1, 3)
plt.stem(np.arange(N), phase_X_k)
plt.title("Phase of X[k]")
plt.xlabel("k")
plt.ylabel("Phase (radians)")

plt.tight_layout()
plt.show()

