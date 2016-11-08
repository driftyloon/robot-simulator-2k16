
import pygame,pygame.locals,random,os,math
import sys

class killerrobot(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.orgimage = pygame.image.load(image)
        self.image=pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 200
        self.speed=4
        self.angle = 0
        self.health=100

    def rotate(self,mousepos):
        self.angle = math.degrees(math.atan2(self.rect.centerx - mousepos[0], self.rect.centery - mousepos[1]))

        self.image = pygame.transform.rotate(self.orgimage, self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def takedamage(self,damage,screen):
        self.health-=damage
        if self.rect.bottom > screen.get_height():
            if self.rect.right > screen.get_width():
                self.rect.centerx-=50
                self.rect.centery-=50
            else:
                self.rect.centerx+=50
                self.rect.centery-=50

        else:
            if self.rect.right > screen.get_width():
                self.rect.centerx-=50
                self.rect.centery+=50
            else:
                self.rect.centerx+=50
                self.rect.centery+=50

        if self.health>0:
            return True
        else:
            return False
    def getangle(self):
        return self.angle

    def getpos(self):
        return [self.rect.centerx,self.rect.centery]


    def go_left(self, screen):
        '''go left, if rect.left is less than 0 no movement occurs'''
        if self.rect.left < 0:
            None
        else:
            self.rect.left -= self.speed

    def go_right(self, screen):
        '''go right, if rect.right is greater than screen width no movement occurs'''
        if self.rect.right > screen.get_width():
            None
        else:
            self.rect.right += self.speed

    def go_up(self, screen):
        '''go up if rect.top is less than screen height no movement occurs'''
        if self.rect.top < 50:
            None
        else:
            self.rect.top -= self.speed

    def go_down(self, screen):
        '''go up if rect.bottom is greater than screen height no movement occurs'''
        if self.rect.bottom > screen.get_height():
            None
        else:
            self.rect.bottom += self.speed

class Text(pygame.sprite.Sprite):
    def __init__(self, size, color, position,variable,message, alpha):
        '''accepts size,color,position,variables,message and alpha'''
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.Font('./AmazDooMRight2.ttf', size)
        self.__color = color
        self.__position = position
        self.variable=variable

        self.message = message
        self.m = ''
        self.__alpha = alpha

    def set_variable(self,variable):
        if variable:
            self.variable=variable
    def setalpha(self,alpha):
            self.__alpha=alpha

    def update(self):
        '''This method will be called automatically to display
        the text at the set position.'''
        if self.variable!=None:
            self.m = self.message+self.variable
        else:
            self.m=self.message
        self.image = self.__font.render(self.m, 1, self.__color)
        self.image.set_alpha(self.__alpha)
        self.rect = self.image.get_rect()
        self.rect.center = (self.__position)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, image,angle,player_pos,mouse_pos,speed,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = player_pos[0]
        self.y = player_pos[1]
        self.damage=damage

        # Assign the mouse target position
        self.targetx = mouse_pos[0]
        self.targety = mouse_pos[1]

        if image:
            self.image=image
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)
            self.image=pygame.transform.rotate\
            (self.image, angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image=pygame.Surface((5,5))
            self.image.fill((255,0,0))
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)

        self.__distance = math.sqrt \
            (pow(self.targetx - self.x, 2) + pow(self.targety - self.y, 2))
        self.animation_steps = self.__distance / speed
        self.dx = (self.targetx - self.x) / self.animation_steps
        self.dy = (self.targety - self.y) / self.animation_steps

    def getdamage(self):
        return self.damage

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top < 0 or self.rect.bottom > 1024 or self.rect.left < 0 or self.rect.right > 1024:
            self.kill()
class enemyBullet(pygame.sprite.Sprite):

    def __init__(self, image,angle,player_pos,mouse_pos,speed,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = player_pos[0]
        self.y = player_pos[1]
        self.damage=damage

        # Assign the mouse target position
        self.targetx = mouse_pos[0]
        self.targety = mouse_pos[1]

        if image:
            self.image=image
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)
            self.image=pygame.transform.rotate\
            (self.image, angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image=pygame.Surface((5,5))
            self.image.fill((255,0,0))
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)

        self.__distance = math.sqrt \
            (pow(self.targetx - self.x, 2) + pow(self.targety - self.y, 2))
        self.animation_steps = self.__distance / speed
        self.dx = (self.targetx - self.x) / self.animation_steps
        self.dy = (self.targety - self.y) / self.animation_steps

    def getdamage(self):
        return self.damage

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top < 0 or self.rect.bottom > 1024 or self.rect.left < 0 or self.rect.right > 1024:
            self.kill()

class enemy(pygame.sprite.Sprite):

    def __init__(self, image,playerpos,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image.convert_alpha()
        self.org=self.image
        self.rect = self.image.get_rect()
        self.speed=3
        self.screen = screen
        self.health=100
        self.spawn()
        self.rotate(playerpos)
        self.set_step_amount(playerpos)

    def spawn(self):
        self.__x = random.randrange(0, -300, -30)
        self.__y = random.randint(0, self.screen.get_height() - 100)
        self.rect.center = (self.__x, self.__y)

    def set_step_amount(self, player_pos):
        try:
            self.distance = math.sqrt \
                (pow(player_pos[0] - self.rect.centerx, 2) + pow(player_pos[1] - self.rect.centery, 2))
            self.__animation_steps = self.distance / self.speed
            self.__dx = (player_pos[0] - self.rect.centerx) / self.__animation_steps
            self.__dy = (player_pos[1] - self.rect.centery) / self.__animation_steps
        except:
            self.__dx = 0
            self.__dy = 0

    def rotate(self,playerpos):
        self.__angle = math.degrees(math.atan2 \
                                        (self.rect.centerx - playerpos[0], self.rect.centery - playerpos[1]))

        self.image = pygame.transform.rotate \
            (self.org, self.__angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def getangle(self):
        return self.__angle

    def damage(self,damagedone):
        self.health-=damagedone
        if self.health>0:
            return True
        else:
            return False

    def update(self):
            self.rect.centerx += self.__dx
            self.rect.centery += self.__dy
class pistolenemy(enemy):
    def __init__(self, image,playerpos,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.org = self.image
        self.screen = screen
        self.speed=2
        self.health=100
        self.fired=0
        self.rect = self.image.get_rect()
        self.rotate(playerpos)
        self.set_step_amount(playerpos)
        self.spawn()

    def spawn(self):
        self.__x = random.randrange(0, -300, -30)
        self.__y = random.randint(0, self.screen.get_height() - 100)
        self.rect.center = (self.__x, self.__y)

    def set_step_amount(self, player_pos):
        try:
            self.distance =( math.sqrt \
                (pow(player_pos[0] - self.rect.centerx, 2) + pow(player_pos[1] - self.rect.centery, 2)))+200
            self.__animation_steps = self.distance / self.speed
            self.__dx = (player_pos[0] - self.rect.centerx) / self.__animation_steps
            self.__dy = (player_pos[1] - self.rect.centery) / self.__animation_steps
        except:
            self.__dx = 0
            self.__dy = 0

    def rotate(self,playerpos):
        self.__angle = math.degrees(math.atan2 \
                                        (self.rect.centerx - playerpos[0], self.rect.centery - playerpos[1]))

        self.image = pygame.transform.rotate \
            (self.org, self.__angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def getangle(self):
        return self.__angle

    def damage(self,damagedone):
        self.health-=damagedone
        if self.health>0:
            return True
        else:
            return False

    def getfired(self):
        return self.fired
    def setfired(self,time):
        self.fired=time

    def update(self):
            self.rect.centerx += self.__dx
            self.rect.centery += self.__dy

class rocketenemy(enemy):
    def __init__(self, image,playerpos,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.org = self.image
        self.screen = screen
        self.speed=2
        self.health=500
        self.fired=0
        self.rect = self.image.get_rect()
        self.rotate(playerpos)
        self.set_step_amount(playerpos)
        self.spawn()

    def spawn(self):
        self.__x = random.randrange(0, -300, -30)
        self.__y = random.randint(0, self.screen.get_height() - 100)
        self.rect.center = (self.__x, self.__y)

    def set_step_amount(self, player_pos):
        try:
            self.distance =( math.sqrt \
                (pow(player_pos[0] - self.rect.centerx, 2) + pow(player_pos[1] - self.rect.centery, 2)))+200
            self.__animation_steps = self.distance / self.speed
            self.__dx = (player_pos[0] - self.rect.centerx) / self.__animation_steps
            self.__dy = (player_pos[1] - self.rect.centery) / self.__animation_steps
        except:
            self.__dx = 0
            self.__dy = 0

    def rotate(self,playerpos):
        self.__angle = math.degrees(math.atan2 \
                                        (self.rect.centerx - playerpos[0], self.rect.centery - playerpos[1]))

        self.image = pygame.transform.rotate \
            (self.org, self.__angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def getangle(self):
        return self.__angle

    def damage(self,damagedone):
        self.health-=damagedone
        if self.health>0:
            return True
        else:
            return False

    def getfired(self):
        return self.fired
    def setfired(self,time):
        self.fired=time

    def update(self):
            self.rect.centerx += self.__dx
            self.rect.centery += self.__dy


class shotgunpickup(pygame.sprite.Sprite):
    def __init__(self, image,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.convert_alpha()
        self.org = self.image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.spawn()

    def spawn(self):
        self.rect.center = (300,200)


class Explosions(pygame.sprite.Sprite):
    def __init__(self, image,screen,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.convert_alpha()
        self.org = self.image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.spawn(position)

    def spawn(self,pos):
        self.rect.center = pos
        newtime = pygame.time.get_ticks()
        oldtime = newtime
        while newtime-oldtime<1000:
            newtime = pygame.time.get_ticks()
            if newtime-oldtime>=100:
               self.kill()
               break

class Rocket(Bullet,pygame.sprite.Sprite):
    def donothing(self):
        x=0
class enemyRocket(Bullet,pygame.sprite.Sprite):
    def donothing(self):
        x=0


def text_objects(text, font):
    textSurface = font.render(text, True, [255,255,255])
    return textSurface, textSurface.get_rect()

def message_display(text,screen):
    largeText = pygame.font.Font('AmazDooMRight2.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1024/2),(768/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    pygame.time.sleep(2)

class button(pygame.sprite.Sprite):
    def __init__(self,msg,x,y,w,h,ic,ac,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen,ac,(x,y,w,h))
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("AmazDooMRight2.ttf",20)
        textSurf,textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
