import pygame
import sys
import math
from queue import PriorityQueue
import uielements  # Importing your UI elements file

clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()

# Set up the display
info = pygame.display.Info()  # Get display information
screen_width, screen_height = info.current_w, info.current_h 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Ship Navigation Algo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Grid properties
grid_size = 4  # Size of each grid cell in pixels
grid_width, grid_height = 550 // grid_size, 600 // grid_size  # Number of cells in each dimension

# Background image positions
map_position = (100, 70)

# Function to draw background
def background():
    image = pygame.image.load("India.jpeg")
    image = pygame.transform.scale(image, (550, 600))
    screen.blit(image, map_position)

# Function to draw foreground (overlay image)
def foreground():
    image = pygame.image.load("IndiaFore.png")
    image = pygame.transform.scale(image, (550, 600))
    screen.blit(image, map_position)

# Function to draw grid over the background
def drawGrid():
    for x in range(map_position[0], map_position[0] + 550, grid_size):
        pygame.draw.line(screen, BLUE, (x, map_position[1]), (x, map_position[1] + 600))
    for y in range(map_position[1], map_position[1] + 600, grid_size):
        pygame.draw.line(screen, BLUE, (map_position[0], y), (map_position[0] + 550, y))

# A* Algorithm
def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star(start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while not open_set.empty():
        _, current = open_set.get()

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                open_set.put((f_score[neighbor], neighbor))

    return None

# Get neighbors for A* (8-way movement)
def get_neighbors(position):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        nx, ny = position[0] + dx, position[1] + dy
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            neighbors.append((nx, ny))
    return neighbors

# Draw the path found by A*
def draw_path(path):
    for cell in path:
        pygame.draw.rect(screen, GREEN, (map_position[0] + cell[0] * grid_size,
                                         map_position[1] + cell[1] * grid_size,
                                         grid_size, grid_size))

# Main loop
running = True
show_input_boxes = False  # Flag to control input box visibility
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if uielements.draw_button(screen, show_input_boxes).collidepoint(event.pos):
                show_input_boxes = not show_input_boxes
            uielements.handle_mouse_click(event)  # Handle mouse click for input boxes if visible

        if show_input_boxes:
            uielements.handle_input(event)

    # Fill the screen with a background color
    screen.fill((0, 0, 140))  # Dark blue background

    # Draw the background image (India map)
    background()

    # Draw the grid over the image
    drawGrid()

    # Draw the foreground overlay
    foreground()

    # Draw the "Manual"/"Automatic" button
    button_rect = uielements.draw_button(screen, show_input_boxes)

    # Conditionally draw the input boxes and labels if the "Manual" button was clicked
    if show_input_boxes:
        uielements.draw_input_boxes(screen)

    # Start A* if coordinates are provided
    if all(uielements.input_boxes):  # Check if all input boxes have values
        try:
            start = (int(uielements.input_boxes[0]), int(uielements.input_boxes[1]))
            end = (int(uielements.input_boxes[2]), int(uielements.input_boxes[3]))
            if 0 <= start[0] < grid_width and 0 <= start[1] < grid_height and \
               0 <= end[0] < grid_width and 0 <= end[1] < grid_height:
                path = a_star(start, end)
                if path:
                    draw_path(path)  # Draw the calculated path
                else:
                    print("Path not found")
            else:
                print("Invalid start or end coordinates")
        except ValueError:
            print("Please enter valid integers for coordinates")

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
