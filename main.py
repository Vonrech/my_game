import pygame

run = True



window = pygame.display.set_mode((480,240))
pygame.display.set_caption("Игроком")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    pygame.display.update()