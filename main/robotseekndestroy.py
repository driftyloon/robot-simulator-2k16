import pygame,pygame.locals,random,os,math
import sys

from main import classdefs

pygame.mixer.init()
pygame.mixer.music.load("./Contra Hard Corps Music.mp3")
pygame.font.init()
pygame.mixer.music.play(-1)
fire = pygame.mixer.Sound("./DSPISTOL.wav")
fireshotgun = pygame.mixer.Sound("./DSSHOTGN.wav")
firerocket = pygame.mixer.Sound("./DSRLAUNC.wav")
fireplasma = pygame.mixer.Sound("./DSPLASMA.wav")
explode= pygame.mixer.Sound("./DSBAREXP.wav")
pain= pygame.mixer.Sound("./DSPLPAIN.wav")
playerdeath=pygame.mixer.Sound("./DSPLDETH.wav")
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
ebullet_hitbox = pygame.sprite.Group()
ebullet_img = pygame.sprite.Group()
rocket_hitbox = pygame.sprite.Group()
rocket_img = pygame.sprite.Group()
erocket_hitbox = pygame.sprite.Group()
erocket_img = pygame.sprite.Group()
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()
robot_group = pygame.sprite.Group()
smartenemies = pygame.sprite.Group()
explosions = pygame.sprite.Group()
enemy_hitbox = pygame.sprite.Group()
warnings = pygame.sprite.Group()
pistolenemies=pygame.sprite.Group()
rocketenemies=pygame.sprite.Group()
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
    global shotgun
    global wave_text
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
    erocket_hitbox.empty()
    erocket_img.empty()
    powerups.empty()
    enemies.empty()
    robot_group.empty()
    explosions.empty()
    enemy_hitbox.empty()
    warnings.empty()
    pistolenemies.empty()
    rocketenemies.empty()
    x=1
    score=0
    robot = classdefs.killerrobot('./temp_sprite.png')
    robot_group.add(robot)
    shotgun = classdefs.shotgunpickup(pygame.image.load('./shotgunicon.png'), screen)
    powerups.add(shotgun)
    renemy1 = classdefs.pistolenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
    rocketenemies.add(renemy1)

    print("lo")
    wave_text = classdefs.Text(50, (0, 0, 0), (500, 50), 0, 'Score:', 255)
    allSprites = pygame.sprite.OrderedUpdates \
        (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies,rocketenemies   ,
         pistolenemies, wave_text, powerups,
         explosions)




def GameOver(score, screen):
    finalscore = classdefs.Text(50, (0, 0, 0), (500, 400), str(score), 'F i n a l   S c o r e :  ', 255)
    screen.fill([255, 255, 255])
    fs = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    fs.add(finalscore)
    button1=classdefs.button("Play Again", 300, 450, 100, 50, green, white,screen)
    button2 = classdefs.button("Quit", 600, 450, 100, 50, red, black,screen)
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
                if pygame.mouse.get_pos()[0]>= 300 and pygame.mouse.get_pos()[0]<= 350:
                    if pygame.mouse.get_pos()[1]>= 450 and pygame.mouse.get_pos()[1]<= 500:
                        x=False
                        running==True
                        reset()
                        break
                elif pygame.mouse.get_pos()[0]>= 600 and pygame.mouse.get_pos()[0]<= 650:
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
wave_text.set_variable(str(score))
allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies,        rocketenemies   ,   pistolenemies, wave_text, powerups,          explosions)
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
                    allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,    rocketenemies   ,       pistolenemies, wave_text, powerups,          explosions)
                    starttime = pygame.time.get_ticks()
                    newtime = 0
                    while starttime - newtime <= 9000:
                        newtime = pygame.time.get_ticks()
                    allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,    rocketenemies   ,       pistolenemies, wave_text, powerups,          explosions)
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
                    allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, erocket_hitbox, erocket_img,robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,          pistolenemies, wave_text, powerups,          explosions)
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
                    allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,          pistolenemies, wave_text, powerups,          explosions)
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
                    allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group,erocket_hitbox, erocket_img, rocket_hitbox, rocket_img, enemies,rocketenemies   ,           pistolenemies, wave_text, powerups,          explosions)
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
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group,erocket_hitbox, erocket_img, rocket_hitbox, rocket_img, enemies, rocketenemies   ,          pistolenemies, wave_text, powerups,          explosions)
            elif gotshotgun==True and weaponselected==2 and pygame.time.get_ticks() - lastfired >= 1200:
                lastfired = pygame.time.get_ticks()
                fireshotgun.play(0)
                bullet1 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, (pygame.mouse.get_pos()[0]+200,pygame.mouse.get_pos()[1]+200), 10, 7)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center, (pygame.mouse.get_pos()[0]+200,pygame.mouse.get_pos()[1]+200), 10, 7)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                bullet2 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 7)
                tracer2 = classdefs.Bullet \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 7)
                bullet_img.add(bullet2)
                bullet_hitbox.add(tracer2)
                bullet3 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, (pygame.mouse.get_pos()[0]-200,pygame.mouse.get_pos()[1]+200), 10, 7)
                tracer3 = classdefs.Bullet \
                    (None, None, robot.rect.center,( pygame.mouse.get_pos()[0]-200,pygame.mouse.get_pos()[1]+200), 10, 7)
                bullet_img.add(bullet3)
                bullet_hitbox.add(tracer3)

            elif gotmachinegun == True and weaponselected == 3:
                rapidfire= True
            elif gotrocketlauncher==True and weaponselected==4 and pygame.time.get_ticks() - lastfired >= 1000:
                lastfired = pygame.time.get_ticks()
                firerocket.play(0)
                rocket = classdefs.Rocket \
                    (pygame.image.load('./rocket.png'), robot.getangle(), \
                     robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                tracer1 = classdefs.Rocket \
                    (None, None, robot.rect.center, pygame.mouse.get_pos(), 10, 5)
                rocket_img.add(rocket)
                rocket_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group,erocket_hitbox, erocket_img, rocket_hitbox, rocket_img, enemies,  rocketenemies   ,         pistolenemies, wave_text, powerups,          explosions)
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
            bullet1 = classdefs.Bullet(pygame.image.load('./shot.png'), robot.getangle(), \
            robot.rect.center, pygame.mouse.get_pos(), 20, 5)
            bullet2 = classdefs.Bullet(None, None, robot.rect.center, pygame.mouse.get_pos(), 10,7)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                      robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies, pistolenemies,rocketenemies   ,
                                                      wave_text, powerups, explosions)
    if rapidfire2:
        plasmarifledelay += 1
    # delay by %3
        if plasmarifledelay % 5 == 0:
            fireplasma.play()
            bullet1 = classdefs.Bullet(pygame.image.load('./plasmabolt.png'), robot.getangle(), \
            robot.rect.center, pygame.mouse.get_pos(), 5, 15)
            bullet2 = classdefs.Bullet(None, None, robot.rect.center, pygame.mouse.get_pos(), 10,10)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                      robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies, pistolenemies,rocketenemies   ,
                                                      wave_text, powerups, explosions)
    for enemy in enemies:
        enemy.rotate(robot.rect.center)
        enemy.set_step_amount(robot.rect.center)
    for pistolenemy in pistolenemies:
        if pygame.time.get_ticks()-pistolenemy.getfired()>700:
            fire.play()
            bullet1 = classdefs.enemyBullet \
                (pygame.image.load('./shot.png'), robot.getangle(), \
                 pistolenemy.rect.center, robot.getpos(), 10, 5)
            tracer1 = classdefs.enemyBullet \
                (None, None, pistolenemy.rect.center, robot.getpos(), 10, 5)
            ebullet_img.add(bullet1)
            ebullet_hitbox.add(tracer1)
            allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,       pistolenemies, wave_text, powerups,          explosions)
            pistolenemy.setfired(pygame.time.get_ticks())
        pistolenemy.rotate(robot.rect.center)
        pistolenemy.set_step_amount(robot.rect.center)

    for rocketenemy in rocketenemies:
        if pygame.time.get_ticks()-rocketenemy.getfired()>700:
            firerocket.play()
            bullet1 = classdefs.enemyRocket \
                (pygame.image.load('./rocket.png'), robot.getangle(), \
                 rocketenemy.rect.center, robot.getpos(), 10, 5)
            tracer1 = classdefs.enemyRocket \
                (None, None, rocketenemy.rect.center, robot.getpos(), 10, 5)
            erocket_img.add(bullet1)
            erocket_hitbox.add(tracer1)
            allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img,ebullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies ,         pistolenemies, wave_text, powerups,          explosions)
            rocketenemy.setfired(pygame.time.get_ticks())
        rocketenemy.rotate(robot.rect.center)
        rocketenemy.set_step_amount(robot.rect.center)
    c = pygame.sprite.groupcollide(bullet_hitbox, enemies,True, False)
    v = pygame.sprite.groupcollide(bullet_img, enemies, True, False)
    if c:
        for bullet in c.keys():
            if not (c[bullet][0].damage(bullet.getdamage())):
                c[bullet][0].kill()
                enemy1 = classdefs.enemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                enemies.add(enemy1)
                score+=100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies,         pistolenemies, wave_text, powerups,          explosions)
    cp = pygame.sprite.groupcollide(ebullet_hitbox, robot_group, True, False)
    vp = pygame.sprite.groupcollide(ebullet_img, robot_group, True, False)
    if cp:
        for bullet in cp.keys():
            if not (cp[bullet][0].takedamage(bullet.getdamage(),screen)):
                robot.kill()
                playerdeath.play(0)
                running==False
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                pain.play(0)
    cr = pygame.sprite.groupcollide(erocket_hitbox, robot_group, True, False)
    vr = pygame.sprite.groupcollide(erocket_img, robot_group, True, False)
    if cr:
        for bullet in cr.keys():
            if not (cr[bullet][0].takedamage(30,screen)):
                robot.kill()
                playerdeath.play(0)
                running==False
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                pain.play(0)

    r = pygame.sprite.groupcollide(rocket_hitbox, enemies, True, False)
    s = pygame.sprite.groupcollide(rocket_img, enemies, True, False)
    if r:
        for rockets in r.keys():
            if not (r[rockets][0].damage(20)):
                r[rockets][0].kill()
                explode.play(0)
                enemy1 = classdefs.enemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                enemies.add(enemy1)
                score += 100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,           pistolenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    c2 = pygame.sprite.groupcollide(bullet_hitbox, pistolenemies,True, False)
    v2 = pygame.sprite.groupcollide(bullet_img, pistolenemies, True, False)
    if c2:
        for bullet in c2.keys():
            if not (c2[bullet][0].damage(bullet.getdamage())):
                c2[bullet][0].kill()
                score += 100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,          pistolenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    c3 = pygame.sprite.groupcollide(bullet_hitbox, rocketenemies,True, False)
    v3 = pygame.sprite.groupcollide(bullet_img, rocketenemies, True, False)
    if c3:
        for bullet in c3.keys():
            if not (c3[bullet][0].damage(bullet.getdamage())):
                c3[bullet][0].kill()
                enemy1 = classdefs.rocketenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                rocketenemies.add(enemy1)
                score+=100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,           rocketenemies, wave_text, powerups,          explosions)
    r4 = pygame.sprite.groupcollide(rocket_hitbox, rocketenemies, True, False)
    s4 = pygame.sprite.groupcollide(rocket_img, rocketenemies, True, False)
    if r4:
        for rockets in r4.keys():
            if not (r4[rockets][0].damage(30)):
                r4[rockets][0].kill()
                explode.play(0)
                enemy1 = classdefs.rocketenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                rocketenemies.add(enemy1)
                score += 100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,          rocketenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)

    e = pygame.sprite.groupcollide(enemies,robot_group,False,False)
    if e:
        for rockets in e.keys():
            if not (robot.takedamage(20,screen)):
                robot.kill()
                playerdeath.play(0)
                running==False
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                score -= 10
                pain.play(0)
    pp = pygame.sprite.groupcollide(pistolenemies,robot_group,False,False)
    if pp:
        for rockets in pp.keys():
            if not (robot.takedamage(30,screen)):
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
