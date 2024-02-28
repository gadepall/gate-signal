import matplotlib.pyplot as plt
import numpy as np

# X-axis
t = np.linspace(0, 1, 201)

# Y-axis
V_c = np.loadtxt("gate23bm30cout.txt")

plt.plot(t, V_c)

plt.xlabel("Time ($t$)")
plt.ylabel("Voltage ($V_c$)")

plt.savefig("plot.png")
