import pygame
pygame.mixer.init()
pygame.init()

musica = input('Escreva a musica desejada: ').strip() .lower()
pygame.mixer.music.load('{}'.format(musica))
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
