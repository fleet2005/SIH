import pygame

# Colors
WHITE = (255, 255, 255)
INPUT_BOX_COLOR = (0, 0, 255)
LABEL_COLOR = (0,0,0)
MANUAL_COLOR_TOP = (255, 100, 100)
MANUAL_COLOR_BOTTOM = (200, 50, 50)
AUTOMATIC_COLOR_TOP = (100, 255, 100)
AUTOMATIC_COLOR_BOTTOM = (50, 200, 50)
BUTTON_TEXT_COLOR = WHITE
BUTTON_BORDER_COLOR = (200, 200, 200)
SHADOW_COLOR = (50, 50, 50)
CLICK_EFFECT_COLOR_TOP = (0, 80, 150)
CLICK_EFFECT_COLOR_BOTTOM = (0, 50, 100)

# Input box properties
input_boxes_position = [(670, 70), (670, 120), (910, 70), (910, 120)]
input_box_width = 50 * 1.8  # Increased by 80%
input_box_height = 40 * 1.1  # Increased by 10%
input_boxes = ["", "", "", ""]
active_box = None


# Function to draw gradient-filled rounded rectangles
def draw_gradient_button(screen, rect, color_top, color_bottom, border_radius=12):
    gradient_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    for y in range(rect.height):
        blend_ratio = y / rect.height
        r = int(color_top[0] * (1 - blend_ratio) + color_bottom[0] * blend_ratio)
        g = int(color_top[1] * (1 - blend_ratio) + color_bottom[1] * blend_ratio)
        b = int(color_top[2] * (1 - blend_ratio) + color_bottom[2] * blend_ratio)
        pygame.draw.line(gradient_surface, (r, g, b), (0, y), (rect.width, y))
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, rect, width=1, border_radius=border_radius)
    screen.blit(gradient_surface, rect.topleft)


# Draw the input boxes with labels
def draw_input_boxes(screen):
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 28)
    labels = ["Departure X:", "Departure Y:", "Destination X ", "Destination Y "]

    for i, pos in enumerate(input_boxes_position):
        label_text = label_font.render(labels[i], True, LABEL_COLOR)
        screen.blit(label_text, (pos[0] - 5, pos[1]))
        pygame.draw.rect(screen, INPUT_BOX_COLOR, (pos[0] + 130, pos[1] - 10, input_box_width, input_box_height), 2)
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
        if pygame.Rect(pos[0] + 130, pos[1] - 10, input_box_width, input_box_height).collidepoint(event.pos):
            active_box = i
            break


# Draw "Manual" / "Automatic" button
def draw_button(screen, show_input_boxes, is_clicked=False):
    button_rect = pygame.Rect(670, 200, 220, 60)

    # Shadow effect
    shadow_rect = button_rect.copy()
    shadow_rect.topleft = (shadow_rect.x + 3, shadow_rect.y + 3)
    pygame.draw.rect(screen, SHADOW_COLOR, shadow_rect, border_radius=8)

    # Button appearance
    if is_clicked:
        draw_gradient_button(screen, button_rect, CLICK_EFFECT_COLOR_TOP, CLICK_EFFECT_COLOR_BOTTOM)
    elif show_input_boxes:
        draw_gradient_button(screen, button_rect, AUTOMATIC_COLOR_TOP, AUTOMATIC_COLOR_BOTTOM)
    else:
        draw_gradient_button(screen, button_rect, MANUAL_COLOR_TOP, MANUAL_COLOR_BOTTOM)

    font = pygame.font.Font(None, 36)
    button_text = "Automatic" if show_input_boxes else "Manual"
    button_text_rendered = font.render(button_text, True, BUTTON_TEXT_COLOR)
    screen.blit(button_text_rendered, (button_rect.centerx - button_text_rendered.get_width() // 2,
                                       button_rect.centery - button_text_rendered.get_height() // 2))
    return button_rect


# Draw "Start" button with modern and on-click effects
def draw_start_button(screen, is_clicked=False):
    button_rect = pygame.Rect(950, 200, 220, 60)

    # Shadow effect
    shadow_rect = button_rect.copy()
    shadow_rect.topleft = (shadow_rect.x + 3, shadow_rect.y + 3)
    pygame.draw.rect(screen, SHADOW_COLOR, shadow_rect, border_radius=8)

    # Button appearance
    if is_clicked:
        draw_gradient_button(screen, button_rect, CLICK_EFFECT_COLOR_TOP, CLICK_EFFECT_COLOR_BOTTOM)
    else:
        draw_gradient_button(screen, button_rect, (0, 150, 255), (0, 100, 200))

    # Button text
    font = pygame.font.Font(None, 36)
    text = font.render("Calculate", True, BUTTON_TEXT_COLOR)
    screen.blit(text, (button_rect.centerx - text.get_width() // 2,
                       button_rect.centery - text.get_height() // 2))
    return button_rect


# Placeholder for "Fuel Estimation" button
def draw_fuel_estimation_button(screen):
    pass


# Placeholder for "Image Analysis" button
def draw_image_analysis_button(screen):
    pass


# Placeholder for "Retrain Model" button
def draw_retrain_model_button(screen):
    pass


# Placeholder for "Path Coordinates" button
def draw_path_coordinates_button(screen):
    pass
