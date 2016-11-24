import random
import pygame

gameOver = True
class asteroidleft:
    
    def __init__(self):
        self.rand_x = random.randint(-90, -30)
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.asteroidw_change = 0
        self.asteroidw = self.rand_x + self.asteroid_thickness
        self.asteroidh = self.rand_y + self.asteroid_thickness
    
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
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            print("Dead")
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])

ship_x = 200
ship_y = 200 
block_size = 50

def rect_overlap(a, b):
    return \
    a[0] < b[0] + b[2] and \
    a[0] + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1]

objects = []
for x in range(10):
    x = asteroidleft()
    objects.append(x)

while 1:
    for x in objects:
        x.move()
