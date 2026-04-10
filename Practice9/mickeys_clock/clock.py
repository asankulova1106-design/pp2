import pygame
from datetime import datetime

mickey = pygame.image.load('images/mainclock.png')
minute_img = pygame.image.load('images/rightarm.png')
second_img = pygame.image.load('images/leftarm.png')

def draw_clock(screen, center):
    time = datetime.now()
    minute = time.minute
    second = time.second

    degree_second = second * 360 / 60
    degree_minute = (minute + second / 60) * 360 / 60




    rot_right = pygame.transform.rotate(minute_img, -degree_minute-45)
    rot_left = pygame.transform.rotate(second_img, -degree_second)

    obj_right = rot_right.get_rect(center=center)
    obj_left = rot_left.get_rect(center=center)

    screen.blit(mickey, (0, 0))
    screen.blit(rot_right, obj_right)
    screen.blit(rot_left, obj_left)