import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

# Colors
background_color = (135, 206, 250)
bird_color = (255, 255, 0)
pipe_color = (0, 128, 0)

# Bird properties
bird_radius = 15
bird_x = 50
bird_y = window_height // 2
bird_velocity = 0
bird_acceleration = 0.5

# Pipe properties
pipe_width = 70
pipe_gap = 200
pipe_velocity = 3

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def create_pipe():
    pipe_height = random.randint(50, 400)
    pipe_x = window_width
    pipe_top = pipe_height
    pipe_bottom = window_height - pipe_height - pipe_gap
    return [pipe_x, pipe_top, pipe_bottom]

def move_pipes(pipes):
    for pipe in pipes:
        pipe[0] -= pipe_velocity

def draw_bird():
    pygame.draw.circle(window, bird_color, (bird_x, bird_y), bird_radius)

def draw_pipes(pipes):
    for pipe in pipes:
        pipe_x, pipe_top, pipe_bottom = pipe
        pygame.draw.rect(window, pipe_color, (pipe_x, 0, pipe_width, pipe_top))
        pygame.draw.rect(window, pipe_color, (pipe_x, window_height - pipe_bottom, pipe_width, pipe_bottom))

def check_collision(pipes):
    for pipe in pipes:
        pipe_x, pipe_top, pipe_bottom = pipe

        if bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < pipe_top or bird_y + bird_radius > window_height - pipe_bottom:
                return True

    if bird_y - bird_radius <= 0 or bird_y + bird_radius >= window_height:
        return True

    return False

def update_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))

pipes = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -8

    window.fill(background_color)

    if len(pipes) == 0 or pipes[-1][0] < window_width - 200:
        pipes.append(create_pipe())

    move_pipes(pipes)
    draw_pipes(pipes)

    bird_velocity += bird_acceleration
    bird_y += bird_velocity
    draw_bird()

    if pipes[0][0] + pipe_width < 0:
        pipes.pop(0)

    if pipes[0][0] < bird_x - bird_radius - pipe_width:
        score += 1

    if check_collision(pipes):
        running = False

    update_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
 
