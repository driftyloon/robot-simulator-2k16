import random
import pygame

gameOver = True
class asteroidleft:
    
    def __init__(self):
        self.rand_x = random.randint(-90, -30)
        self.rand_y = 200 #random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.asteroidw_change = 0
        self.asteroidw = self.rand_x + self.asteroid_thickness
        self.asteroidh = self.rand_y + self.asteroid_thickness
        print(self.rand_x)
        print(self.rand_y)
        print(self.asteroidw)
        print(self.asteroidh)
    def move(self):
        if self.rand_x < 0:
            self.rand_x_change += 10
            self.asteroidw_change += 10
        if self.rand_x > 1350:
            self.rand_x_change += -10
            self.asteroidw_change += - 10
        self.rand_x += self.rand_x_change
        self.asteroidw += self.asteroidw_change
        print("x = " + str(self.rand_x))
        print("y = " + str(self.rand_y))
        print("x width = " + str(self.asteroidw))
        print("y width = " + str(self.asteroidh))
        if self.asteroidw >= ship_x and self.asteroidh >= ship_y and self.asteroidw <= ship_xw and self.asteroidh <= ship_yw:
            print("You're Dead!!")
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])

ship_x = 200
ship_y = 200
ship_xw = 200+50
ship_yw = 200+50

x = asteroidleft()
while 1:
    x.move()
    pygame.time.delay(100)
