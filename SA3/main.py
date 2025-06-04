import pygame
from nanobot import NanoBot  # Import the NanoBot class
from bacteria import Bacteria

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")
# Create character instance
FPS=60
clock=pygame.time.Clock()


# Game loop
# Main game loop - Displaying Player
nanobot_laser_group = pygame.sprite.Group()

nanobot_group = pygame.sprite.Group()
nanobot = NanoBot(nanobot_laser_group)
nanobot_group.add(nanobot)

bacteria_group = pygame.sprite.Group()
bacteria_laser_group=pygame.sprite.Group()

num_rows = 5
num_cols = 11
start_x = 100
start_y = 50
spacing_x = 100  # horizontal spacing between bacteria
spacing_y = 70   # vertical spacing between rows

for row in range(num_rows):
    for col in range(num_cols):
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y
        # Provide velocity (e.g., 2) and bullet_group (nanobot_laser_group)
        bacteria = Bacteria(x, y, 2, bacteria_laser_group)
        bacteria_group.add(bacteria)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            nanobot.fire()

    screen.fill((0, 0, 0))  # Clear the screen before drawing

    # Update and draw the player
    nanobot_group.update(event)
    nanobot_group.draw(screen)

    nanobot_laser_group.update()
    nanobot_laser_group.draw(screen)

     
    bacteria_group.update()
    bacteria_group.draw(screen)

    
    bacteria_laser_group.update()
    bacteria_laser_group.draw(screen)
    
    bacteria_group.update()
    bacteria_group.draw(screen)

    
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
