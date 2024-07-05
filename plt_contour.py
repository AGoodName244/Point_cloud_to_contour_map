import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Generate random data points
np.random.seed(0)  # For reproducibility
x = np.random.uniform(-3, 3, 100)
y = np.random.uniform(-2, 2, 100)
z = np.sin(x) * np.cos(y)  # Example function for z values

# Create grid values first
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
X, Y = np.meshgrid(xi, yi)

# Interpolate the data
Z = griddata((x, y), z, (X, Y), method='cubic')

# Create the contour plot
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, levels=15, linewidths=0.5, colors='k')
CSF = ax.contourf(X, Y, Z, levels=15, cmap='viridis')

# Adding labels to contours
manual_locations = [(xi[10], yi[20]), (xi[30], yi[40]), (xi[50], yi[60]), (xi[70], yi[80]), (xi[90], yi[90])]
ax.clabel(CS, inline=True, fontsize=10, manual=manual_locations)

# Setting the title and labels
ax.set_title('Contour plot from random data points')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Show the plot
plt.colorbar(CSF)
plt.show()
