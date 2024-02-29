import numpy as np
import matplotlib.pyplot as plt

def transfer_function(s):
    return 10000/ (s**2 + 2*s + 10000)

# Frequency range (adjust as needed)
f_min = 0.1
f_max = 200
num_points = 1000  # Number of frequency points

# Linear spacing
w = np.linspace(f_min, f_max, num_points)  # Logarithmic spacing

# Evaluate transfer function at frequencies 
H = transfer_function(1j * w)

# Calculate magnitude and phase
mag = 20 * np.log10(np.abs(H))
phase = np.rad2deg(np.angle(H))
phase_unwrapped = phase.copy()  # Create a copy to avoid modifying original data

for i in range(2, len(phase)):
    jump = phase_unwrapped[i] - phase_unwrapped[i-1]
    if jump >= 180:  # Handle positive jumps exceeding 180 degrees
        for i in range(i,len(phase)):
            phase_unwrapped[i] -= 360
    elif jump <= -180:  # Handle negative jumps exceeding 180 degrees
        for i in range(i,len(phase)):
            phase_unwrapped[i] += 360





# Create the plot
plt.figure(figsize=(8, 6))  # Adjust figure size if needed

# Magnitude plot
plt.subplot(2, 1, 1)
plt.plot(w, mag, label='Magnitude (dB)')
plt.grid(True)
plt.ylabel('Magnitude (dB)')

# Phase plot
plt.subplot(2, 1, 2)
plt.plot(w, phase_unwrapped, label='Phase (deg)')
plt.grid(True)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (deg)')

# Legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("A.png")
