import pygame
import pygame.mixer
pygame.init()

run = True

score = 0

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




window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Amongus vs Asteroids")


# music
pygame.mixer.music.load("music/bg.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.75)


#Pictures import

bg = pygame.transform.scale(pygame.image.load("image/bg.png"),(width,height))

player_img = pygame.transform.scale(pygame.image.load("image/player.png"),(64,64))


floor = pygame.transform.scale(pygame.image.load("image/floor.png"),(800,25))
walles = pygame.transform.scale(pygame.image.load("image/walls.png"),(25,600))
brick_s = pygame.transform.scale(pygame.image.load("image/brick_s.png"),(100,25))
brick_up = pygame.transform.scale(pygame.image.load("image/brick_up.png"),(25,100))
enemy = pygame.transform.scale(pygame.image.load("image/enemy.png"),(64,64))
oxygen = pygame.transform.scale(pygame.image.load("image/oxygen.png"),(32,32))


#Player Spawn

start_x = 50
start_y = 50 

#Creating groups

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()



#Creating objects 

player = Object(player_img, start_x, start_y, 5)
all_sprites.add(player) 



#Creating walls



floor_up = Object(floor,0,575,0)
floor_down = Object(floor,0,0,0)
wall_left = Object(walles,0,0,0)
wall_right = Object(walles,775,0,0)
walls.add(floor_up,floor_down,wall_left,wall_right)
all_sprites.add(floor_up,floor_down,wall_left,wall_right)


brick_1 = Object(brick_s,1,132,0)
brick_2 = Object(brick_s,101,132,0)
brick_3 = Object(brick_up,201,132,0)
brick_4 = Object(brick_up,376,132,0)
brick_5 = Object(brick_up,201,232,0)
brick_6 = Object(brick_up,376,232,0)
brick_7 = Object(brick_s,201,332,0)
brick_8 = Object(brick_s,301,332,0)
brick_9 = Object(brick_up,575,132,0)
brick_10 = Object(brick_up,575,232,0)
brick_11 = Object(brick_up,575,332,0)
brick_12 = Object(brick_s,500,457,0)
brick_13 = Object(brick_s,400,457,0)
brick_14 = Object(brick_s,300,457,0)
brick_15 = Object(brick_up,575,357,0)
brick_16 = Object(brick_up,201,499,0)
brick_17 = Object(brick_up,201,475,0)
brick_18 = Object(brick_s,200,457,0)

walls.add(brick_1,brick_2,brick_3,brick_4,brick_5,brick_6,brick_7,brick_8,brick_9,brick_10,brick_11,brick_12,brick_13,brick_14,brick_15,brick_16,brick_17,brick_18)
all_sprites.add(brick_1,brick_2,brick_3,brick_4,brick_5,brick_6,brick_7,brick_8,brick_9,brick_10,brick_11,brick_12,brick_13,brick_14,brick_15,brick_16,brick_17,brick_18)

# enemies

enemy_1 = Object(enemy,270,250,5)
enemy_2 = Object(enemy,70,500,2)
enemies.add(enemy_1,enemy_2)
all_sprites.add(enemy_1,enemy_2)

# "coins"

oxygen1 = Object(oxygen, 100,200,0)
oxygen2 = Object(oxygen, 300,500,0)
oxygen3 = Object(oxygen, 250,400,0)
items.add(oxygen1,oxygen2,oxygen3)
all_sprites.add(oxygen1,oxygen2,oxygen3)



#text 
oxygen_font = pygame.font.Font(None, 35)
oxygen_text = oxygen_font.render("Кислород: 0", True, pygame.Color("light blue"))



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

    # walls collision

    if len(pygame.sprite.spritecollide(player, walls, False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y 

    # enemy move

    enemy_1.rect.y += enemy_1.speed
    if len(pygame.sprite.spritecollide(enemy_1, walls, False)) > 0:
        enemy_1.speed *= -1
    if len(pygame.sprite.spritecollide(enemy_1, items, False)) > 0:
        enemy_1.speed *= -1
    enemy_2.rect.y += enemy_2.speed
    if len(pygame.sprite.spritecollide(enemy_2, walls, False)) > 0:
        enemy_2.speed *= -1
    if len(pygame.sprite.spritecollide(enemy_2, items, False)) > 0:
        enemy_2.speed *= -1



    # enemy collision

    if len(pygame.sprite.spritecollide(player, enemies, False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y 



    # get points
    if len(pygame.sprite.spritecollide(player, items, True)) > 0:
        score += 1
        oxygen_text = oxygen_font.render(("Кислород: " + str(score)), True, pygame.Color("light blue"))


    all_sprites.draw(window)
    all_sprites.update()

    window.blit(oxygen_text,(500,0))
    
    pygame.display.update()