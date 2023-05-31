import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # 1. init the parent class
        self.image = pygame.image.load('../graphics/background.png').convert_alpha()  # surface -> image
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2)) # rect

# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('meteor shooter 2')
clock = pygame.time.Clock()

# sprite groups
spaceship_group = pygame.sprite.Group()

# sprite creation
ship = Ship()
spaceship_group.add(ship)






# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # delta time
    dt = clock.tick() / 1000
    
    # graphics
    spaceship_group.draw(display_surface)
    
    # draw the frame
    pygame.display.update()