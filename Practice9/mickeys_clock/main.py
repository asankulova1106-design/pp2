import pygame
from clock import draw_clock

pygame.init()
screen = pygame.display.set_mode((833, 843))
center = (833//2, 843//2)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_clock(screen, center)
    pygame.display.flip()

pygame.quit()