import pygame
from random import randrange

WIDTH  = 800
LENGHT = 800
HEIGHT = 800

OFFSET = (WIDTH/2, HEIGHT/2)

screen = pygame.display.set_mode((WIDTH, LENGHT))

def map_nums(nb, X_1, X_2, Y_1, Y_2):

    offset = (Y_1-X_1)

    nb = nb+offset
    nb = nb*((Y_1-Y_2)/(X_1-X_2))

    return nb

class Star(object):
    
    def __init__(self):
        
        self.x = (randrange(-5000,5000))
        self.y = (randrange(-5000,5000))
        self.z = 799

        self.size = 1

    def show(self):

        pygame.draw.circle(screen, (255, 255, 255), (int(self.x+OFFSET[0]), int(self.y+OFFSET[1])), int(self.size))

    def move(self):

        self.size = self.z*0.001*(800-self.z)

        self.x = map_nums(self.x/self.z, 0, 1, 0, WIDTH)
        self.y = map_nums(self.y/self.z, 0, 1, 0, LENGHT)

        if self.x>WIDTH/2 or self.y>HEIGHT/2 or self.x<-WIDTH/2 or self.y<-WIDTH/2:
            self.__init__()


        self.z -= 0.001

liste_etoiles = []
for _ in range(300):
    S = Star()
    liste_etoiles.append(S)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((10, 10, 10,))


    for etoile in liste_etoiles:
        etoile.show()
        etoile.move()

    pygame.display.flip()