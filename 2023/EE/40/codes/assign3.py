import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data = np.loadtxt('assign3.dat')

# Extract V_in and V_out values
V_in = data[:, 0]
V_out = data[:, 1]

# Plot the graph
plt.plot(V_in, V_out, color='blue')
plt.ylim(0, 5.5)
plt.xlabel('$V_{in}$ in $mV$ (Analog Input)')
plt.ylabel('Digital Output in Hex')

x_ticks = [0, 9.8, 19.6, 39.2, 58.8, 78.4, 98]
plt.xticks(x_ticks, x_ticks)

y_ticks = [1, 2, 3, 4, 5]
y_tick_labels = list(map(lambda y: '{:02d}H'.format(int(y)), y_ticks))
plt.yticks(y_ticks, y_tick_labels)

plt.grid(True)
plt.savefig('assign3.png')
plt.show()
