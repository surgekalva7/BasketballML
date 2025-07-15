import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the basketball court dimensions
court_width = 94  # Court width in feet (NBA standard)
court_height = 50  # Court height in feet (NBA standard)

# Create the figure and axis for the court visualization
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, court_width)
ax.set_ylim(0, court_height)
ax.set_aspect('equal', adjustable='box')

# Draw the court boundaries
ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_height, court_height, 0], color='black')

# Initialize the dot indicator
dot, = ax.plot([], [], 'ro', markersize=10, label='Detected Position')
ax.legend()

def update_dot(position):
    if position:
        # Ensure position is valid and scale it
        scaled_x = position[0] / 10  # Example scaling factor (adjust based on image resolution)
        scaled_y = position[1] / 10  # Example scaling factor (adjust based on image resolution)
        dot.set_data([scaled_x], [scaled_y])  # Pass as sequences (lists or tuples)
    else:
        # If no position detected, hide the dot by setting it outside the court
        dot.set_data([], [])  # Empty sequences to hide the dot
    return dot,

def visualize_live_positions(get_position_callback):
    def update(frame):
        # Get the latest position from the callback
        position = get_position_callback()
        return update_dot(position)

    ani = FuncAnimation(fig, update, interval=100)
    plt.show()