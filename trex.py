#print ("hello world")
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Dino
dino = pygame.Rect(80, 220, 40, 60)
dino_vel_y = 0
on_ground = True
GRAVITY = 1
JUMP_FORCE = -18

# Cactus
cactus = pygame.Rect(800, 230, 20, 50)
cactus_speed = 7

score = 0
running = True

while running:
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, 280), (WIDTH, 280), 2)  # ground

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                dino_vel_y = JUMP_FORCE
                on_ground = False

    # Gravity
    dino_vel_y += GRAVITY
    dino.y += dino_vel_y
    if dino.y >= 220:
        dino.y = 220
        dino_vel_y = 0
        on_ground = True

    # Move cactus
    cactus.x -= cactus_speed
    if cactus.x < -30:
        cactus.x = WIDTH + random.randint(200, 500)
        score += 1

    # Collision
    if dino.colliderect(cactus):
        print(f"Game Over! Score: {score}")
        running = False

    pygame.draw.rect(screen, BLACK, dino)
    pygame.draw.rect(screen, RED, cactus)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
