# Basketball Out-of-Bounds Play Detection Model

## Overview
This project focuses on developing a machine learning model to detect whether a basketball play is out of bounds. By analyzing player positions, ball movements, and court boundaries, the model aims to provide accurate and real-time decisions to assist referees and improve game fairness.

## Features
- **Boundary Detection**: Identifies court boundary lines to determine in-bounds and out-of-bounds areas.
- **Ball Tracking**: Detects the basketball and tracks its movement during gameplay.
- **Impact Analysis**: Determines where the ball hits the ground and whether it lands on or outside the boundary line.
- **Player Positioning**: Detects player locations and identifies which side of the boundary line they are on.
- **Violation Detection**: Determines if a player is out of bounds while touching the ball.
- **Last Touch Analysis**: Identifies the last player to touch the ball before it goes out of bounds.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/BasketballML.git
    ```
2. Navigate to the project directory:
    ```bash
    cd BasketballML
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Connect your drone or camera system to the application.
2. Start capturing game footage.
3. Analyze out-of-bounds plays and view insights on the dashboard.

## TODOs
1. Implement functionality to detect court boundary lines.
2. Develop ball detection and tracking capabilities.
3. Add logic to determine where the ball hits the ground and its position relative to the boundary line.
4. Enable detection of player positions and their relation to the boundary line.
5. Implement checks for players being out of bounds while touching the ball.
6. Create a system to identify the last player to touch the ball before it goes out of bounds.