import pygame
pygame.init()


width = 300
height = 300
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
x = width/2
y = height/2
radius = 25
speed = 20


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x <= speed + radius:
                    x = radius
                else:
                    x -= speed

            if event.key == pygame.K_RIGHT:
                if x >= width - (speed+radius):
                    x = width - radius
                else:
                    x += speed
            if event.key == pygame.K_UP:
                if y <= speed + radius:
                    y = radius
                else:
                    y -= speed

            if event.key == pygame.K_DOWN:
                if y >= height - (speed+radius):
                    y = height - radius
                else:
                    y += speed
                     
  
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25) 
    
    pygame.display.flip()

pygame.quit()
