import pygame
import pathFunction

class Frog(pygame.sprite.Sprite):
    """
    Frog class gives an object of an enemy frog
    parameters:
    x = horisontal line
    y = vertical line
    image = picture
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('./mimages/frogMonster1.png')

    def show_frog(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_you_fool(self, speed):
        if(self.x < -100):
            self.x = 700
        self.x -= speed

    def bool(self, Px, Py,Fx,Fy):
        """
        This function is to check if player hits enemy
        parameters:
        Px = player x
        Py = player y
        Fx = Monster x
        Fy = monster Y
        """
        if Px >= Fx -40 and Px <= Fx+80 \
        and Py >= Fy -30 and Py <= Fy+30:

            return True
        else:
            False
           
  

        
