import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#List of Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 128, 0)

#Fills in the background.  Sets a background Color
display_surface.fill(PURPLE)

#Draws a Circle
CENTER = (300, 300)
RADIUS = 50
pygame.draw.circle(display_surface, YELLOW, (200, 200), RADIUS, 25)
pygame.draw.circle(display_surface, YELLOW, (400, 200), RADIUS, 25)
pygame.draw.circle(display_surface, YELLOW, (200, 200), 15, 5)
pygame.draw.circle(display_surface, YELLOW, (400, 200), 15, 5)


#Draw a Line
#START = (100, 100)
#END = (500, 500)
#pygame.draw.line(display_surface, RED, START, END, 50)

#Draw a Rectangle
TOP_LEFT_X = 100
TOP_LEFT_Y = 350
WIDTH = 400
HEIGHT = 150
rect = pygame.Rect(TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, YELLOW, rect, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()