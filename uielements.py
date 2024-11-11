# ui_elements.py
import pygame

# Colors
WHITE = (255, 255, 255)
INPUT_BOX_COLOR = (0, 0, 255)
LABEL_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 100, 200)
BUTTON_TEXT_COLOR = WHITE

# Input box properties
input_boxes_position = [(670, 70), (670, 120), (910, 70), (910, 120)]
input_boxes = ["", "", "", ""]
active_box = None

# Draw the input boxes with labels
def draw_input_boxes(screen):
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 28)
    labels = ["Departure X:", "Departure Y:", "Destination X ", "Destination Y "]

    for i, pos in enumerate(input_boxes_position):
        label_text = label_font.render(labels[i], True, LABEL_COLOR)
        screen.blit(label_text, (pos[0] - 5, pos[1]))
        pygame.draw.rect(screen, INPUT_BOX_COLOR, (pos[0] + 130, pos[1] - 10, 50, 40), 2)
        text = font.render(input_boxes[i], True, WHITE)
        screen.blit(text, (pos[0] + 135, pos[1] - 3))

# Handle keyboard input for the active box
def handle_input(event):
    global active_box
    if active_box is not None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_boxes[active_box] = input_boxes[active_box][:-1]
            elif event.key == pygame.K_RETURN:
                pass
            else:
                input_boxes[active_box] += event.unicode

# Handle mouse click to select the active input box
def handle_mouse_click(event):
    global active_box
    for i, pos in enumerate(input_boxes_position):
        if pygame.Rect(pos[0] + 130, pos[1] - 10, 50, 40).collidepoint(event.pos):
            active_box = i
            break

# Draw "Manual" / "Automatic" button
def draw_button(screen, show_input_boxes):
    font = pygame.font.Font(None, 36)
    button_text = "Automatic" if show_input_boxes else "Manual"
    button_text_rendered = font.render(button_text, True, BUTTON_TEXT_COLOR)
    button_rect = pygame.Rect(670, 200, 120, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    screen.blit(button_text_rendered, (button_rect.x + 15, button_rect.y + 10))
    return button_rect

def draw_start_button(screen):
    button_color = (0, 200, 0)  # Green button color
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Start", True, (255, 255, 255))  # White text
    button_rect = pygame.Rect(950, 200, 120, 50)  # Position and size of the button
    pygame.draw.rect(screen, button_color, button_rect)  # Draw button
    screen.blit(text, (button_rect.x + 20, button_rect.y + 10))  # Center the text
    return button_rect