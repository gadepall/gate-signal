import matplotlib.pyplot as plt

# Read data from output_expression.txt
with open('output_expression.txt', 'r') as file:
    data_expression = [line.split('\t') for line in file.readlines()]
    x_expression = [float(line[0].split('=')[1]) for line in data_expression]
    y_expression = [float(line[1].split('=')[1]) for line in data_expression]

# Read data from output.txt
with open('output.txt', 'r') as file:
    data_integration = [line.split('\t') for line in file.readlines()]
    x_integration = [float(line[0].split('=')[1]) for line in data_integration]
    y_integration = [float(line[1].split('=')[1]) for line in data_integration]

# Plot the results on the same set of axes
plt.figure(figsize=(10, 5))

# Plot for expression 3e^x - 2(x+1)
plt.plot(x_expression, y_expression, label='3e^x - 2(x+1)')

# Plot for numerical integration y(n) = y(n-1) + h/6 * [2x(n-1) + y(n-1)(6+3h+h^2+h^3/4) + (6h+2h^2+h^3/2)]
plt.plot(x_integration, y_integration, label='Numerical Integration')

# Add labels and legend
plt.title('Comparison of Expressions')
plt.xlabel('x')
plt.ylabel('Result')
plt.legend()

plt.savefig("grap.png")
