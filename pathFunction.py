import os
import pygame


def get_image_path(path):
    """
    This file/function is so i dont have to rewrite it everytime i want to laod
    in images ( Sprites or background)
    Parameter:
    path = will be the path to the pictures

    return:
        A list with the images
    """
    the_imgs = []
  
    for image_file in os.listdir(path):
        image = pygame.image.load(path + os.sep + image_file)
        the_imgs.append(image)
    return the_imgs

        