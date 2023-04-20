# --------------------------------------------------------------------------------------------------------

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My UI")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Define the font
font = pygame.font.Font(None, 36)

# Define the button rectangle
button_rect = pygame.Rect(100, 100, 200, 50)

# Start the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the button
    pygame.draw.rect(screen, GRAY, button_rect)
    text = font.render("Click me!", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()