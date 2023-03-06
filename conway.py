import numpy as np
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))

def draw_grid(paused):
    screen.fill(WHITE)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if paused:
        font = pygame.font.Font(None, 36)
        text = font.render("PAUSED", True, GRAY)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
    pygame.display.update()

def update_grid():
    global grid
    new_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
    for x in range(1, GRID_WIDTH-1):
        for y in range(1, GRID_HEIGHT-1):
            neighbors = int(grid[x-1, y-1] + grid[x-1, y] + grid[x-1, y+1] + grid[x, y-1] + grid[x, y+1] + grid[x+1, y-1] + grid[x+1, y] + grid[x+1, y+1])
            if grid[x, y] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[x, y] = 1
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    grid = new_grid

def add_cells(pos):
    global grid
    cell_x = pos[0] // CELL_SIZE
    cell_y = pos[1] // CELL_SIZE
    grid[cell_x, cell_y] = 1
    draw_grid(False)

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            add_cells(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Si se presiona la tecla 'p'
                paused = not paused # Cambiar el estado de la pausa
    if not paused:
        update_grid()
    draw_grid(paused)
