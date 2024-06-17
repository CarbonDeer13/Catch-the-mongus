import pygame
import random
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the mongus")

# Load images
player_img = pygame.transform.scale(pygame.image.load('player.png'), (80, 80))
object_img = pygame.transform.scale(pygame.image.load('object.png'), (50, 50))
player_rect = player_img.get_rect(center=(400, 550))
PLAYER_SPEED = 15

clock = pygame.time.Clock()
objects = []
score = 0
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_rect.right < 800:
        player_rect.x += PLAYER_SPEED
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_rect.top > 0:
        player_rect.y -= PLAYER_SPEED
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_rect.bottom < 600:
        player_rect.y += PLAYER_SPEED

    # Drop objects
    if random.randint(1, 20) == 1:
        objects.append(object_img.get_rect(topleft=(random.randint(0, 750), -50)))

    # Move objects and check for collisions
    for obj in objects[:]:
        obj.y += 7
        if obj.colliderect(player_rect):
            score += 1
            objects.remove(obj)
        elif obj.top > 600:
            objects.remove(obj)

    # Drawing
    screen.fill((255, 255, 255))
    screen.blit(player_img, player_rect)
    for obj in objects:
        screen.blit(object_img, obj)
    # Display your name on the game screen
    name_text = pygame.font.Font(None, 36).render('Created by Pranish', True, (0, 0, 255))
    screen.blit(name_text, (10, 80))
    # Display score and timer
    screen.blit(pygame.font.Font(None, 36).render(f'Score: {score}', True, (0, 0, 0)), (10, 10))
    screen.blit(pygame.font.Font(None, 36).render(f'Time Left: {60 - int(elapsed_time)}s', True, (255, 0, 0)), (10, 50))
    pygame.display.flip()

    if elapsed_time > 60:
        running = False
    clock.tick(60)

# End screen
screen.fill((255, 255, 255))
end_text = pygame.font.Font(None, 50).render(f"Time's up! Your Score: {score}", True, (0, 0, 0))
screen.blit(end_text, (250, 250))
# Display your name on the end screen
credit_text = pygame.font.Font(None, 40).render('Game by Pranish', True, (0, 0, 255))
screen.blit(credit_text, (280, 350))
pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
sys.exit()
