import pygame,pygame.locals,random,os,math
import sys

from main import classdefs

pygame.mixer.init()
pygame.mixer.music.load("./main/Contra Hard Corps Music.mp3")
pygame.font.init()
##pygame.mixer.music.play(-1)
fire = pygame.mixer.Sound("./main/DSPISTOL.wav")
fireshotgun = pygame.mixer.Sound("./main/DSSHOTGN.wav")
firerocket = pygame.mixer.Sound("./main/DSRLAUNC.wav")
fireplasma = pygame.mixer.Sound("./main/DSPLASMA.wav")
explode= pygame.mixer.Sound("./main/DSBAREXP.wav")
pain= pygame.mixer.Sound("./main/DSPLPAIN.wav")
playerdeath=pygame.mixer.Sound("./main/DSPLDETH.wav")
pygame.display.set_caption("Robot simulator 2016")
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1024,768))
rect=screen.get_rect()
black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
red = (200,0,0)
bullet_hitbox = pygame.sprite.Group()
bullet_img = pygame.sprite.Group()
rocket_hitbox = pygame.sprite.Group()
rocket_img = pygame.sprite.Group()
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()
robot_group = pygame.sprite.Group()
smartenemies = pygame.sprite.Group()
explosions = pygame.sprite.Group()
enemy_hitbox = pygame.sprite.Group()
warnings = pygame.sprite.Group()
global x
global score
def reset():
    global rapidfire
    global rapidfire2
    global lastfired
    global gotshotgun
    global gotmachinegun
    global gotplasmarifle
    global gotrocketlauncher
    global running
    global machinegundelay
    global plasmarifledelay
    global weaponselected
    global allSprites
    global x
    global score
    global robot
    rapidfire=False
    rapidfire2=False
    lastfired=0;
    gotshotgun=False
    gotmachinegun=True
    gotplasmarifle=True
    gotrocketlauncher=True
    running=True
    machinegundelay=0
    plasmarifledelay=0
    weaponselected=1
    bullet_hitbox.empty()
    bullet_img.empty()
    rocket_hitbox.empty()
    rocket_img.empty()
    powerups.empty()
    enemies.empty()
    robot_group.empty()
    explosions.empty()
    enemy_hitbox.empty()
    warnings.empty()
    x=1
    score=0
    allSprites = pygame.sprite.OrderedUpdates \
        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies,powerups,explosions)
    robot = classdefs.killerrobot('./main/temp_sprite.png')
    robot_group.add(robot)
    shotgun = classdefs.shotgunpickup(pygame.image.load('./main/shotgunicon.png'), screen)
    powerups.add(shotgun)
    enemy1 = classdefs.enemy(pygame.image.load('./main/temp_sprite.png'), robot.rect.center, screen)
    enemies.add(enemy1)
    print("lo")




def GameOver(score, screen):
    finalscore = classdefs.Text(50, (0, 0, 0), (500, 400), str(score), 'F i n a l   S c o r e :  ', 255)
    screen.fill([255, 255, 255])
    fs = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    fs.add(finalscore)
    button1=classdefs.button("Play Again", 150, 450, 100, 50, green, white,screen)
    button2 = classdefs.button("Quit", 550, 450, 100, 50, red, black,screen)
    buttons.add(button1)
    buttons.add(button2)
    display = pygame.sprite.OrderedUpdates \
        (fs,buttons)
    display.update()
    display.draw(screen)
    pygame.display.flip()
    x=True

    while x==True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if pygame.mouse.get_pos()[0]>= 150 and pygame.mouse.get_pos()[0]<= 250:
                    if pygame.mouse.get_pos()[1]>= 450 and pygame.mouse.get_pos()[1]<= 500:
                        x=False
                        running==True
                        reset()
                elif pygame.mouse.get_pos()[0]>= 550 and pygame.mouse.get_pos()[0]<= 650:
                    if pygame.mouse.get_pos()[1]>= 450 and pygame.mouse.get_pos()[1]<= 500:
                        sys.exit(0)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(60)
        display.update()
        display.draw(screen)
        pygame.display.flip()
wave_text = classdefs.Text(50, (0, 0, 0), (500, 50), 0, 'Score:', 255)
reset()
allSprites = pygame.sprite.OrderedUpdates \
    (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups, explosions)
wave_text.set_variable(str(score))
allSprites.draw(screen)
while running==True:
    clock.tick(60)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.locals.K_w]:
        robot.go_up(screen)
    if keystate[pygame.locals.K_a]:
        robot.go_left(screen)
    if keystate[pygame.locals.K_s]:
        robot.go_down(screen)
    if keystate[pygame.locals.K_d]:
        robot.go_right(screen)
    newtime = pygame.time.get_ticks()

    for event in pygame.event.get():
        oldtime = newtime
        newtime = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.key == pygame.K_1:
                rapidfire = False
                rapidfire2= False
                weaponselected = 1
            elif event.key == pygame.K_2:
                rapidfire = False
                rapidfire2= False
                if gotshotgun==True:
                    weaponselected = 2
                else:
                    noshotgun = classdefs.Text(50, (0, 0, 0), (500, 205), None, 'You dont have the shotgun!', 255)
                    warnings.add(noshotgun)
                    allSprites = pygame.sprite.OrderedUpdates \
                        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text,
                         powerups,explosions)
                    starttime = pygame.time.get_ticks()
                    newtime = 0
                    while starttime - newtime <= 9000:
                        newtime = pygame.time.get_ticks()
                    allSprites = pygame.sprite.OrderedUpdates \
                        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text,
                         powerups,explosions)
                    weaponselected = 1

            elif event.key == pygame.K_3:
                rapidfire = False
                rapidfire2= False
                if gotmachinegun == True:
                    weaponselected = 3
                    rapidfire==False
                else:
                    nomg = classdefs.Text(50, (0, 0, 0), (500, 502), None, 'You dont have the rocketlauncher!', 255)
                    warnings.add(norl)
                    allSprites = pygame.sprite.OrderedUpdates \
                        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text,
                         powerups,explosions)
                    starttime = pygame.time.get_ticks()
                    newtime = 0
                    while starttime - newtime < 900:
                        newtime = pygame.time.get_ticks()
                        if starttime-newtime<900:
                            nomg.kill()
                    weaponselected = 1

            elif event.key == pygame.K_4:
                rapidfire = False
                rapidfire2= False
                if gotrocketlauncher == True:
                    weaponselected = 4
                else:
                    norl = classdefs.Text(50, (0, 0, 0), (500, 502), None, 'You dont have the rocketlauncher!', 255)
                    warnings.add(norl)
                    allSprites = pygame.sprite.OrderedUpdates \
                        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text,
                         powerups,explosions)
                    starttime = pygame.time.get_ticks()
                    newtime = 0
                    while starttime - newtime < 900:
                        newtime = pygame.time.get_ticks()
                        if starttime-newtime<900:
                            norl.kill()
                    weaponselected = 1
            elif event.key == pygame.K_5:
                if gotplasmarifle == True:
                    weaponselected = 5
                    rapidfire = False
                    rapidfire2 = False
                else:
                    nopr = classdefs.Text(50, (0, 0, 0), (500, 502), None, 'You dont have the rocketlauncher!', 255)
                    warnings.add(nopr)
                    allSprites = pygame.sprite.OrderedUpdates \
                        (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text,
                         powerups,explosions)
                    starttime = pygame.time.get_ticks()
                    newtime = 0
                    while starttime - newtime < 900:
                        newtime = pygame.time.get_ticks()
                        if starttime-newtime<900:
                            nopr.kill()
                    weaponselected = 1



        elif  event.type == pygame.MOUSEBUTTONDOWN:
            if weaponselected==1 and pygame.time.get_ticks() - lastfired >= 500:
                lastfired = pygame.time.get_ticks()
                fire.play(0)
                bullet1 = classdefs.Bullet \
                    (pygame.image.load('./main/shot.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates \
                    (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups,
                    explosions)
            elif gotshotgun==True and weaponselected==2 and pygame.time.get_ticks() - lastfired >= 1200:
                lastfired = pygame.time.get_ticks()
                fireshotgun.play(0)
                bullet1 = classdefs.Bullet \
                    (pygame.image.load('./main/shot.png'), robot.getangle(), \
                     robot.rect.center, (pygame.mouse.get_pos()[0]+200,pygame.mouse.get_pos()[1]+200), 10, 7)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center, (pygame.mouse.get_pos()[0]+200,pygame.mouse.get_pos()[1]+200), 10, 7)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                bullet2 = classdefs.Bullet \
                    (pygame.image.load('./main/shot.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 7)
                tracer2 = classdefs.Bullet \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 7)
                bullet_img.add(bullet2)
                bullet_hitbox.add(tracer2)
                bullet3 = classdefs.Bullet \
                    (pygame.image.load('./main/shot.png'), robot.getangle(), \
                     robot.rect.center, (pygame.mouse.get_pos()[0]-200,pygame.mouse.get_pos()[1]+200), 10, 7)
                tracer3 = classdefs.Bullet \
                    (None, None, robot.rect.center,( pygame.mouse.get_pos()[0]-200,pygame.mouse.get_pos()[1]+200), 10, 7)
                bullet_img.add(bullet3)
                bullet_hitbox.add(tracer3)
                allSprites = pygame.sprite.OrderedUpdates \
                    (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups,
                    explosions)
            elif gotmachinegun == True and weaponselected == 3:
                rapidfire= True
            elif gotrocketlauncher==True and weaponselected==4 and pygame.time.get_ticks() - lastfired >= 1000:
                lastfired = pygame.time.get_ticks()
                firerocket.play(0)
                rocket = classdefs.Rocket \
                    (pygame.image.load('./main/rocket.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                tracer1 = classdefs.Rocket \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                rocket_img.add(rocket)
                rocket_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates \
                    (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups,
                    explosions)
            elif gotplasmarifle == True and weaponselected == 5:
                rapidfire2= True
        elif event.type == pygame.MOUSEBUTTONUP:
            if weaponselected == 3:
               rapidfire= False
            if weaponselected==5:
                rapidfire2=False

    if rapidfire:
        machinegundelay += 1
    # delay by %3
        if machinegundelay % 5 == 0:
            fire.play()
            bullet1 = classdefs.Bullet(pygame.image.load('./main/shot.png'), robot.getangle(), \
            robot.rect.center, pygame.mouse.get_pos(), 10, 5)
            bullet2 = classdefs.Bullet(None, None, robot.rect.center, pygame.mouse.get_pos(), 10,7)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates \
                (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups,
                explosions)
    if rapidfire2:
        plasmarifledelay += 1
    # delay by %3
        if plasmarifledelay % 5 == 0:
            fireplasma.play()
            bullet1 = classdefs.Bullet(pygame.image.load('./main/plasmabolt.png'), robot.getangle(), \
            robot.rect.center, pygame.mouse.get_pos(), 10, 10)
            bullet2 = classdefs.Bullet(None, None, robot.rect.center, pygame.mouse.get_pos(), 10,10)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates \
                (bullet_img, bullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies, wave_text, powerups,
                explosions)
    for enemy in enemies:
        enemy.rotate(robot.rect.center)
        enemy.set_step_amount(robot.rect.center)
    c = pygame.sprite.groupcollide(bullet_hitbox, enemies,True, False)
    v = pygame.sprite.groupcollide(bullet_img, enemies, True, False)
    if c:
        for bullet in c.keys():
            if not (c[bullet][0].damage(bullet.getdamage())):
                c[bullet][0].kill()
                enemy1 = classdefs.enemy(pygame.image.load('./main/temp_sprite.png'), robot.rect.center, screen)
                enemies.add(enemy1)
                score+=100
    r = pygame.sprite.groupcollide(rocket_hitbox, enemies, True, False)
    s = pygame.sprite.groupcollide(rocket_img, enemies, True, False)
    if r:
        for rockets in r.keys():
            if not (r[rockets][0].damage(20)):
                r[rockets][0].kill()
                explode.play(0)
                enemy1 = classdefs.enemy(pygame.image.load('./main/temp_sprite.png'), robot.rect.center, screen)
                enemies.add(enemy1)
                score += 100
            else:
                explode.play(0)

    e = pygame.sprite.groupcollide(enemies,robot_group,False,False)
    if e:
        for rockets in e.keys():
            if not (robot.takedamage(20)):
                robot.kill()
                playerdeath.play(0)
                running==False
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                score -= 10
                pain.play(0)
    p = pygame.sprite.groupcollide(robot_group, powerups, False, False)
    if p:
        shotgun.kill()
        gotshotgun=True
    wave_text.set_variable(str(score))
    screen.fill([255,255,255])
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
