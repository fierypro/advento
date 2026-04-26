import matplotlib.pyplot as plt
import numpy as np

# Initial Conditions
speed = float(input("Initial Speed of Projectile in m/s: "))
angle = float(input("Initial Angle of Projectile in degrees: "))
theta = np.radians(angle)
g = 9.8

x, y = 0, 0
time = 0
dt = 0.001

# Components
vx = speed * np.cos(theta)
vy = speed * np.sin(theta)

# Height and Range
projectile_range = (pow(speed, 2) * np.sin(2 * theta)) / g
maximum_height = pow(vy, 2) / (2 * g)

# Points to plot
x_values = []
y_values =[]

details = f"""
Initial speed : {speed} m/s
Angle         : {angle} degrees
Range         : {projectile_range:.2f} m 
Height        : {maximum_height:.2f} m
"""

while y >= 0:
    x_values.append(x)
    y_values.append(y)

    x += vx * dt
    y += vy * dt

    vy -= g * dt
    time += dt

plt.plot(x_values, y_values)
plt.title("Projectile Motion Simulation")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()

print(details)
