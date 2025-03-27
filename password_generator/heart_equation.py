import numpy as np
import matplotlib.pyplot as plt

# Define the grid for x and y values
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# Define the heart equation
F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# Plot the contour where F = 0 (the heart shape)
plt.contour(X, Y, F, levels=[0], colors='red')

# Make the plot visually appealing
plt.title("Heart Shape Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", linewidth=0.5)

# Show the plot
plt.show()
