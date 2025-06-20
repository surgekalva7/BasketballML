# FILE: boundary_detection.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import random

def draw_basketball_court(ax):
    # Court dimensions (in feet)
    court_length = 94  # Full court length
    court_width = 50   # Full court width
    three_point_radius = 23.75  # Three-point line radius
    free_throw_radius = 6  # Free throw circle radius
    key_width = 16  # Width of the key
    key_height = 19  # Height of the key

    # Draw the outer boundary
    outer_boundary = patches.Rectangle((0, 0), court_length, court_width, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(outer_boundary)

    # Draw the center circle
    center_circle = patches.Circle((court_length / 2, court_width / 2), free_throw_radius, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(center_circle)

    # Draw the key areas
    left_key = patches.Rectangle((0, (court_width - key_width) / 2), key_height, key_width, linewidth=2, edgecolor='black', facecolor='none')
    right_key = patches.Rectangle((court_length - key_height, (court_width - key_width) / 2), key_height, key_width, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(left_key)
    ax.add_patch(right_key)

    # Draw the three-point arcs
    left_three_point_arc = patches.Arc((0, court_width / 2), three_point_radius * 2, three_point_radius * 2, theta1=-90, theta2=90, linewidth=2, edgecolor='black')
    right_three_point_arc = patches.Arc((court_length, court_width / 2), three_point_radius * 2, three_point_radius * 2, theta1=90, theta2=270, linewidth=2, edgecolor='black')
    ax.add_patch(left_three_point_arc)
    ax.add_patch(right_three_point_arc)

    # Set axis limits and aspect ratio
    ax.set_xlim(-5, court_length + 5)
    ax.set_ylim(-5, court_width + 5)
    ax.set_aspect('equal', adjustable='box')

def update(frame, ball, court_length, court_width):
    # Simulate random ball movement
    ball.set_center((random.uniform(0, court_length), random.uniform(0, court_width)))
    return ball,

def main():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 7))

    # Draw the basketball court
    draw_basketball_court(ax)

    # Add a ball to the court
    ball = patches.Circle((47, 25), radius=1, color='orange')
    ax.add_patch(ball)

    # Animate the ball movement
    #ani = FuncAnimation(fig, update, fargs=(ball, 94, 50), interval=500)

    # Display the court
    plt.title("Live Basketball Court Model")
    plt.show()

if __name__ == "__main__":
    main()