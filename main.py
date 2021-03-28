import pygame

run = True

height = 640
width = 800

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed 




window = pygame.display.set_mode((800,655))
pygame.display.set_caption("Amongus vs Asteroids")


#Pictures import

bg = pygame.transform.scale(pygame.image.load("image/bg.png"),(width,height))

player_img = pygame.transform.scale(pygame.image.load("image/player.png"),(64,64))

wall = pygame.transform.scale(pygame.image.load("image/wall.png"),(50,50))

#Player Spawn

start_x = 50
start_y = 50 

#Creating groups

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()



#Creating objects 

player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player) 



#Creating walls

wall1 = Object(wall,0,0,0)
wall2 = Object(wall,32,0,0)
wall3 = Object(wall,64,0,0)
wall4 = Object(wall,96,0,0)
wall5 = Object(wall,128,0,0)
wall6 = Object(wall,160,0,0)
wall7 = Object(wall,192,0,0)
wall8 = Object(wall,224,0,0)
wall9 = Object(wall,256,0,0)
wall10 = Object(wall,288,0,0)
wall11 = Object(wall,320,0,0)
wall12 = Object(wall,352,0,0)
wall13 = Object(wall,384,0,0)
wall14 = Object(wall,416,0,0)
wall15 = Object(wall,448,0,0)
wall16 = Object(wall,480,0,0)
wall17 = Object(wall,512,0,0)
wall18 = Object(wall,544,0,0)
wall19 = Object(wall,576,0,0)
wall20 = Object(wall,608,0,0)
wall21 = Object(wall,640,0,0)
wall22 = Object(wall,672,0,0)
wall23 = Object(wall,704,0,0)
wall24 = Object(wall,736,0,0)
wall25 = Object(wall,768,0,0)


wall1y = Object(wall,0,0,0)
wall2y = Object(wall,0,32,0)
wall3y = Object(wall,0,64,0)
wall4y = Object(wall,0,96,0)
wall5y = Object(wall,0,128,0)
wall6y = Object(wall,0,160,0)
wall7y = Object(wall,0,192,0)
wall8y = Object(wall,0,224,0)
wall9y = Object(wall,0,256,0)
wall10y = Object(wall,0,288,0)
wall11y = Object(wall,0,320,0)
wall12y = Object(wall,0,352,0)
wall13y = Object(wall,0,384,0)
wall14y = Object(wall,0,416,0)
wall15y = Object(wall,0,448,0)
wall16y = Object(wall,0,480,0)
wall17y = Object(wall,0,512,0)
wall18y = Object(wall,0,544,0)
wall19y = Object(wall,0,576,0)
wall20y = Object(wall,0,608,0)
wall21y = Object(wall,0,640,0)



walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25)
all_sprites.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25)

walls.add(wall1y,wall2y,wall3y,wall4y,wall5y,wall6y,wall7y,wall8y,wall9y,wall10y,wall11y,wall12y,wall13y,wall14y,wall15y,wall16y,wall17y,wall18y,wall19y,wall20y,wall21y)
all_sprites.add(wall1y,wall2y,wall3y,wall4y,wall5y,wall6y,wall7y,wall8y,wall9y,wall10y,wall11y,wall12y,wall13y,wall14y,wall15y,wall16y,wall17y,wall18y,wall19y,wall20y,wall21y)



wall1d = Object(wall,0,608,0)
wall2d = Object(wall,32,608,0)
wall3d = Object(wall,64,608,0)
wall4d = Object(wall,96,608,0)
wall5d = Object(wall,128,608,0)
wall6d = Object(wall,160,608,0)
wall7d = Object(wall,192,608,0)
wall8d = Object(wall,224,608,0)
wall9d = Object(wall,256,608,0)
wall10d = Object(wall,288,608,0)
wall11d = Object(wall,320,608,0)
wall12d = Object(wall,352,608,0)
wall13d = Object(wall,384,608,0)
wall14d = Object(wall,416,608,0)
wall15d = Object(wall,448,608,0)
wall16d = Object(wall,480,608,0)
wall17d = Object(wall,512,608,0)
wall18d = Object(wall,544,608,0)
wall19d = Object(wall,576,608,0)
wall20d = Object(wall,608,608,0)
wall21d = Object(wall,640,608,0)
wall22d = Object(wall,672,608,0)
wall23d = Object(wall,704,608,0)
wall24d = Object(wall,736,608,0)
wall25d = Object(wall,768,608,0)

walls.add(wall1d,wall2d,wall3d,wall4d,wall5d,wall6d,wall7d,wall8d,wall9d,wall10d,wall11d,wall12d,wall13d,wall14d,wall15d,wall16d,wall17d,wall18d,wall19d,wall20d,wall21d,wall22d,wall23d,wall24d,wall25d)
all_sprites.add(wall1d,wall2d,wall3d,wall4d,wall5d,wall6d,wall7d,wall8d,wall9d,wall10d,wall11d,wall12d,wall13d,wall14d,wall15d,wall16d,wall17d,wall18d,wall19d,wall20d,wall21d,wall22d,wall23d,wall24d,wall25d)


wall1y2 = Object(wall,768,0,0)
wall2y2 = Object(wall,768,32,0)
wall3y2 = Object(wall,768,64,0)
wall4y2 = Object(wall,768,96,0)
wall5y2 = Object(wall,768,128,0)
wall6y2 = Object(wall,768,160,0)
wall7y2 = Object(wall,768,192,0)
wall8y2 = Object(wall,768,224,0)
wall9y2 = Object(wall,768,256,0)
wall10y2 = Object(wall,768,288,0)
wall11y2 = Object(wall,768,320,0)
wall12y2 = Object(wall,768,352,0)
wall13y2 = Object(wall,768,384,0)
wall14y2 = Object(wall,768,416,0)
wall15y2 = Object(wall,768,448,0)
wall16y2 = Object(wall,768,480,0)
wall17y2 = Object(wall,768,512,0)
wall18y2 = Object(wall,768,544,0)
wall19y2 = Object(wall,768,576,0)
wall20y2 = Object(wall,768,608,0)
wall21y2 = Object(wall,768,640,0)

walls.add(wall1y2,wall2y2,wall3y2,wall4y2,wall5y2,wall6y2,wall7y2,wall8y2,wall9y2,wall10y2,wall11y2,wall12y2,wall13y2,wall14y2,wall15y2,wall16y2,wall17y2,wall18y2,wall19y2,wall20y2,wall21y2)
all_sprites.add(wall1y2,wall2y2,wall3y2,wall4y2,wall5y2,wall6y2,wall7y2,wall8y2,wall9y2,wall10y2,wall11y2,wall12y2,wall13y2,wall14y2,wall15y2,wall16y2,wall17y2,wall18y2,wall19y2,wall20y2,wall21y2)


wall1x2 = Object(wall,50,128,0)
wall2x2 = Object(wall,100,128,0)
wall3x2 = Object(wall,150,128,0)
wall4x2 = Object(wall,200,128,0)
wall5x2 = Object(wall,250,128,0)
wall6x2 = Object(wall,200,278,0)
wall7x2 = Object(wall,150,278,0)
wall8x2 = Object(wall,300,278,0)
wall9x2 = Object(wall,350,278,0)

walls.add(wall1x2,wall2x2,wall3x2,wall4x2,wall5x2,wall6x2,wall7x2,wall8x2,wall9x2)
all_sprites.add(wall1x2,wall2x2,wall3x2,wall4x2,wall5x2,wall6x2,wall7x2,wall8x2,wall9x2)

wall1y3 = Object(wall,250,178,0)
wall2y3 = Object(wall,250,228,0)
wall3y3 = Object(wall,250,278,0)
wall4y3 = Object(wall,400,178,0)
wall5y3 = Object(wall,400,228,0)
wall6y3 = Object(wall,400,278,0)
wall7y3 = Object(wall,400,128,0)

walls.add(wall1y3,wall2y3,wall3y3,wall4y3,wall5y3,wall6y3,wall7y3)
all_sprites.add(wall1y3,wall2y3,wall3y3,wall4y3,wall5y3,wall6y3,wall7y3)


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