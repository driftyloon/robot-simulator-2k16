import pygame,pygame.locals,random,os,math
import sys

from main import classdefs
pygame.mixer.init()
pygame.mixer.music.load("./main/Contra Hard Corps Music.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Robot simulator 2016")
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1024,768))
rect=screen.get_rect()
running=True
bullet_hitbox=pygame.sprite.Group()
bullet_img=pygame.sprite.Group()
enemies=pygame.sprite.Group()
x=1
robot= classdefs.killerrobot('./main/temp_sprite.png')
robot_group = pygame.sprite.RenderPlain(robot)
allSprites = pygame.sprite.OrderedUpdates\
    (bullet_img,bullet_hitbox,robot,enemies)
while running:
    clock.tick(30)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.locals.K_w]:
        robot.go_up(screen)
    if keystate[pygame.locals.K_a]:
        robot.go_left(screen)
    if keystate[pygame.locals.K_s]:
        robot.go_down(screen)
    if keystate[pygame.locals.K_d]:
        robot.go_right(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif  event.type == pygame.MOUSEBUTTONDOWN:
            bullet1 = classdefs.Bullet \
                (pygame.image.load('./main/shot.png'), robot.getangle(), \
                 robot.rect.center, pygame.mouse.get_pos(), 10, 5)
            bullet2 = classdefs.Bullet \
                (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 5)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates \
                (bullet_img, bullet_hitbox,robot,enemies)
    if x<2:
        enemy1 = classdefs.enemy(pygame.image.load('./main/temp_sprite.png'),robot.rect.center,screen)
        enemies.add(enemy1)
        allSprites = pygame.sprite.OrderedUpdates \
            (bullet_img, bullet_hitbox, robot, enemies)
        x+=1
    for enemy in enemies:
        enemy.rotate(robot.rect.center)
        enemy.set_step_amount(robot.rect.center)
    screen.fill([255,255,255])
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
