import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("output.txt", skiprows=1)

# clear all the previous figures
plt.close("all")
# plot the graph
y_n = data[:11]
plt.stem(range(1, len(data) + 1), y_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.scatter(range(1, len(data) + 1), data, color='red',marker='x',s=100,label=r'Analysis')
plt.xticks(range(1, len(data) + 1))
# Plotting
plt.xlabel('n')
plt.ylabel('$L_n$')
# Add legend
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")
