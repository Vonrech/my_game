import pygame

run = True

height = 600
width = 800

class Objects(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed 


bg = pygame.transform.scale(pygame.image.load("img/bg.png"),(width,height))

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Игроком")
while run:

    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





    pygame.display.update()