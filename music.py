import pygame

def menu_music():
    pygame.mixer.music.load('./gameMusic/menuSong.wav')
    return pygame.mixer.music.play()

def game_music():
    pygame.mixer.music.load('./gameMusic/mySuperGameSong.wav')
    return pygame.mixer.music.play()
