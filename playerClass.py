import pygame
import pathFunction


class Player(pygame.sprite.Sprite):
    """
    Inside this class i create a player object out of png images
    """
    def __init__(self, position, images):
        pygame.sprite.Sprite.__init__(self)
        size = (32,32)

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_turn_right = images
        # THis below will flip all my sprites so that it turns in the direction i press
        self.images_turn_left = [pygame.transform.flip(img,True,False) for img in images]
        self.index = 0
        # In pygame "image" will be the current pic of animation
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0,0)

        self.anim_time = 0.1
        self.current_time = 0

    def update_animation(self,time):
        """
        This function handles how the images will be turned
        if player press x = + then it is bigger than 0.
        So it loads the images_turn_right. And the other do the opposite
        """
        if self.velocity.x > 0:
            self.images = self.images_turn_right
        elif self.velocity.x < 0:
            self.images = self.images_turn_left

        self.current_time += time
        if self.current_time >= self.anim_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)        


