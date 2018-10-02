import pygame

def play_mp3(mp3, syncronous=True):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    if syncronous:
        while pygame.mixer.music.get_busy() == True:
            pass
