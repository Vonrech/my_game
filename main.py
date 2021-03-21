import pygame

run = True

height = 600
width = 800

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed 




window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Amongus vs Asteroids")


#Pictures import

bg = pygame.transform.scale(pygame.image.load("image/bg.png"),(width,height))

player_img = pygame.transform.scale(pygame.image.load("image/player.png"),(64,64))

#Player Spawn

start_x = 100
start_y = 120 




#Creating groups

all_sprites = pygame.sprite.Group()



#Creating objects 

player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player) 













while run:

    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_UP]:
            player.rect.y -= player.speed
        if keys[pygame.K_DOWN]:
            player.rect.y += player.speed
        if keys[pygame.K_RIGHT]:
            player.image = pygame.transform.flip(player_img,False,False)
            player.rect.x += player.speed
        if keys[pygame.K_LEFT]:
            player.image = pygame.transform.flip(player_img,True,False)
            player.rect.x -= player.speed


    all_sprites.draw(window)
    all_sprites.update()
    
    pygame.display.update()