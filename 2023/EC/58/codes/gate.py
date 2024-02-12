import numpy as np
import matplotlib.pyplot as plt


t_values = np.linspace(-5, 5, 1000)  

x2_values = np.zeros_like(t_values)  


index_minus_3 = np.abs(t_values + 3).argmin()
index_2 = np.abs(t_values - 2).argmin()


x2_values[index_minus_3] = 1
x2_values[index_2] = 2

plt.plot(t_values, x2_values, label='x2(t)', color='black')


plt.annotate('', xy=(t_values[index_minus_3], 1), xytext=(t_values[index_minus_3], 0),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.1, headwidth=4))
plt.annotate('', xy=(t_values[index_2], 2), xytext=(t_values[index_2], 0),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.1, headwidth=4))

plt.plot([-1, -1], [0, 1], color='black', linestyle='-', linewidth=2.0)
plt.plot([1, 1], [0, 1], color='black', linestyle='-', linewidth=2.0)


plt.hlines(1, -1, 1, color='black', linestyle='-', linewidth=2.0)


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))


plt.yticks([1, 2])

plt.text(-0.3, 1.5, 'x2(t)', rotation=90, verticalalignment='center')

plt.xlabel('t')
plt.grid(False)
plt.legend()
plt.show()

