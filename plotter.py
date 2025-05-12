import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
initial_height = 1.0
initial_period = 2.0
initial_w_m = 5.0
initial_w_p = 10.0

# Function to plot
def compute_plot(x, height, period, w_m, w_p):
    return height * np.sin(2 * np.pi * x / period) * np.exp(-((x - w_m)**2) / w_p)

# Create figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
x = np.linspace(0, 20, 400)
y = compute_plot(x, initial_height, initial_period, initial_w_m, initial_w_p)
[line] = ax.plot(x, y)
ax.set_title("Interactive Plot with Sliders")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Define sliders
slider_height_ax = plt.axes([0.1, 0.25, 0.8, 0.03])
slider_period_ax = plt.axes([0.1, 0.2, 0.8, 0.03])
slider_w_m_ax = plt.axes([0.1, 0.15, 0.8, 0.03])
slider_w_p_ax = plt.axes([0.1, 0.1, 0.8, 0.03])

slider_height = Slider(slider_height_ax, "Height", 0.1, 5.0, valinit=initial_height)
slider_period = Slider(slider_period_ax, "Period", 0.5, 10.0, valinit=initial_period)
slider_w_m = Slider(slider_w_m_ax, "w_m", 0.0, 20.0, valinit=initial_w_m)
slider_w_p = Slider(slider_w_p_ax, "w_p", 1.0, 20.0, valinit=initial_w_p)

# Update function
def update(val):
    height = slider_height.val
    period = slider_period.val
    w_m = slider_w_m.val
    w_p = slider_w_p.val
    line.set_ydata(compute_plot(x, height, period, w_m, w_p))
    fig.canvas.draw_idle()

# Connect sliders to update function
slider_height.on_changed(update)
slider_period.on_changed(update)
slider_w_m.on_changed(update)
slider_w_p.on_changed(update)

plt.show()

