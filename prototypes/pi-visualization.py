# Source: https://www.youtube.com/shorts/aUDYWYqtAR4

import numpy as np
import matplotlib.pyplot as plt

# Create an array of theta values in degrees (e.g., from 0 to 113*360 degrees)
theta_degrees = np.linspace(0, 113*360, 10000)

# Convert degrees to radians
theta_radians = np.deg2rad(theta_degrees)

# Calculate z(theta) using the formula, 1j is the imaginary number
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)

# Separate the real and imaginary parts of z
x = np.real(z)
y = np.imag(z)

# Create a plot with specific settings
plt.figure(figsize=(10, 10), facecolor='black')  # Set figure background to black
plt.plot(x, y, color='white', linewidth=0.5)  # White lines
plt.gca().set_facecolor('black')  # Set axis background to black
plt.axis('off')  # Turn off axes
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding
plt.show()
