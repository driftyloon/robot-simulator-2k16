import random
import pygame

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

        
class asteroidright:
    
    def __init__(self):
        self.rand_x = random.randint(1351, 1400)
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
    def move(self):
        random_change = random.randint(10,100)
        if self.rand_x < -90:
            self.rand_x_change += 10
        if self.rand_x > 1350:
            self.rand_x_change += -10
        self.rand_x += self.rand_x_change
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            print("Dead")
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])

class asteroidup:
    
    def __init__(self):
        self.rand_x = random.randint(0, 1240)
        self.rand_y = random.randint(-90,-30)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.rand_y_change = 0
    def move(self):
        if self.rand_y < -20:
            self.rand_y_change += 10
        if self.rand_y > 800:
            self.rand_y_change += -10
        self.rand_y += self.rand_y_change
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            print("Dead")
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])


pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
fps = 30

BLACK = 0,0,0
GREY = 126,126,126
RED = 255,0,0

ship_x = (width/2)-25
ship_y = (height/2)-25
block_size = 50

def rect_overlap(a, b):
    return \
    a[0] < b[0] + b[2] and \
    a[0] + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1]

    
objectsleft = []
for o in range(5):
    asteroid1 = asteroidleft()
    objectsleft.append(asteroid1)

objectsright = []
for a in range(5):
    asteroid2 = asteroidright()
    objectsright.append(asteroid2)

objectsup = []
for b in range(5):
    asteroid3 = asteroidup()
    objectsup.append(asteroid3)

def gameLoop():
    gameOver = False
    
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                gameOver = True

        screen.fill(BLACK)
        for asteroid1 in objectsleft:
            asteroid1.draw()
        for asteroid2 in objectsright:
            asteroid2.draw()
        for asteroid3 in objectsup:
            asteroid3.draw()
        for asteroid1 in objectsleft:
            asteroid1.move()
        for asteroid2 in objectsright:
            asteroid2.move()
        for asteroid3 in objectsup:
            asteroid3.move()
        pygame.draw.rect(screen, RED, [ship_x,ship_y,block_size,block_size])
        pygame.display.flip()
        clock.tick(fps)

gameLoop()
pygame.quit()
        
