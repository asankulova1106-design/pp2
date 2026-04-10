import pygame, time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
font = pygame.font.Font(None, 30)

playlist = ["music/audio1.mp3", "music/audio2.mp3"]
names = ["Empty", "Zombie"]

i = 0
pygame.mixer.music.load(playlist[i])

duration = int(pygame.mixer.Sound(playlist[i]).get_length())
start = 0
done = False

while not done:
    screen.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_p:
                pygame.mixer.music.play()
                start = time.time()

            if e.key == pygame.K_s:
                pygame.mixer.music.stop()
                start = 0

            if e.key in (pygame.K_n, pygame.K_b):
                i = 1 - i
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                start = time.time()
                duration = int(pygame.mixer.Sound(playlist[i]).get_length())

            if e.key == pygame.K_q:
                done = True

    t = int(time.time() - start) if start else 0

    screen.blit(font.render(names[i], True, (255,255,255)), (20,30))
    screen.blit(font.render(f"{t} / {duration} sec", True, (255,255,255)), (20,80))
    screen.blit(font.render("P - play  S - stop  N/B - switch  Q - quit", True, (200, 200, 200)), (20, 200))

    pygame.display.flip()

pygame.quit()