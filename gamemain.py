import pygame

pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (700, 500)
done = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)##, pygame.FULLSCREEN)
pygame.display.set_caption("Killer Robot Simulator 2K16")


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
