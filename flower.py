import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌸 Flower Click Game 🌸")

# Colors
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

# Load flower image
flower_img = pygame.image.load("flower.jpg")  
flower_img = pygame.transform.scale(flower_img, (60, 60))

# Font
font = pygame.font.SysFont("Arial", 28)

# Ask user for settings
print("🌸 Welcome to the Flower Game!")
game_time = int(input("⏳ Enter game time in seconds: "))
difficulty = input("🎮 Choose difficulty (easy/medium/hard): ").lower()

# Difficulty speed
if difficulty == "easy":
    spawn_rate = 1200
elif difficulty == "hard":
    spawn_rate = 500
else:
    spawn_rate = 800

# Game variables
score = 0
flowers = []
clock = pygame.time.Clock()
start_time = time.time()

# Timers
SPAWN_FLOWER = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_FLOWER, spawn_rate)

running = True
while running:
    screen.fill(PINK)

    # Time left
    elapsed = int(time.time() - start_time)
    time_left = game_time - elapsed

    if time_left <= 0:
        running = False

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Spawn flower
        if event.type == SPAWN_FLOWER:
            x = random.randint(50, WIDTH - 100)
            y = random.randint(50, HEIGHT - 100)
            flowers.append(pygame.Rect(x, y, 60, 60))

        # Click flower
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for f in flowers[:]:
                if f.collidepoint(mx, my):
                    flowers.remove(f)
                    score += 1

    # Draw flowers
    for f in flowers:
        screen.blit(flower_img, f.topleft)

    # UI
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    time_text = font.render(f"Time Left: {time_left}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    pygame.display.update()
    clock.tick(60)

# Game over
screen.fill(WHITE)
end_text = font.render(f"⏰ Time's up! Final Score: {score}", True, (0, 0, 0))
screen.blit(end_text, (WIDTH//2 - 200, HEIGHT//2))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
