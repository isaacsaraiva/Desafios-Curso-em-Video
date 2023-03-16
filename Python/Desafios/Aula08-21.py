import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Henrique_e_Juliano_-_LIBERDADE_PROVISORIA_-_DVD_Ao_Vivo_No_Ibirapuera.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
