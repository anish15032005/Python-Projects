import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Dynamic Heart Animation", fontsize=14, fontweight='bold', color='red')
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)
ax.grid(True, linestyle="--", linewidth=0.5)

# Create a line object (empty at the start)
line, = ax.plot([], [], 'r', linewidth=2)

# Generate points for the heart curve
t = np.linspace(0, 2 * np.pi, 500)  # Parameter for the heart curve
x = 16 * np.sin(t) ** 3 / 16
y = (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) / 16

# Initialization function: plot the background
def init():
    line.set_data([], [])
    return line,

# Animation function: draws the heart shape dynamically
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=10, blit=True)

# Show the animation
plt.show()
