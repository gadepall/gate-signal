import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
with open("frequency_response_data.txt", "r") as file:
    lines = file.readlines()
    # Extract transfer function numerator coefficients
    numerator_coeffs = [float(line.strip()) for line in lines[1:4]]
    # Extract transfer function denominator coefficients
    denominator_coeffs = [float(line.strip()) for line in lines[6:10]]
    # Extract phase crossover frequency
    phase_crossover_freq = float(lines[11].split(":")[1].strip().split()[0])

# Create transfer function from coefficients
sys = signal.TransferFunction(numerator_coeffs, denominator_coeffs)

# Frequency response
w, mag, phase = signal.bode(sys)

# Convert phase from degrees to radians
phase_rad = phase * np.pi / 180

# Plot both the magnitude and phase response on a single graph
plt.figure(figsize=(10, 6))

# Magnitude response plot
plt.semilogx(w, mag, color='blue', label='Magnitude Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# Phase response plot
plt.semilogx(w, phase_rad, color='orange', label='Phase Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (radians)')
plt.grid(True)

# Mark the phase crossover frequency
plt.scatter(phase_crossover_freq, -np.pi, color='red')
plt.text(phase_crossover_freq*1.5, -np.pi*1.5, f'{phase_crossover_freq:.2f} rad/s (Phase Crossover Frequency)', color='red')

plt.title('Frequency Response')
plt.legend()
plt.tight_layout()
plt.show() 


