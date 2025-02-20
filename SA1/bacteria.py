import pygame
import random
class Bacteria(pygame.sprite.Sprite):
    """A class to model an enemy alien"""
    
    def __init__(self, x, y, velocity, laser_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("SA1/bacteria.png")
        new_size = (50, 50) 
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.direction = 1
        self.velocity = velocity
        self.laser_group = laser_group

        
    def update(self):
        """Update the alien"""
        self.rect.x += self.direction*self.velocity

        
   