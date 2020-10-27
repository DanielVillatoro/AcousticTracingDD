
# Pruebas de PIL
from PIL import Image
import numpy as np
import pygame


imagen1 = np.array(Image.open('imagenprueba.jpg'))
imagen2 = np.array(Image.open('imagenprueba.jpg'))


def modificarPixeles():
    for i in range(500):
        for j in range(500):
            if(np.array_equiv(imagen1[i,j],255)):
                imagen1[i,j] = 5


# UI
h,w=1200,800
border=50
pygame.init()
screen = pygame.display.set_mode((h, w))
pygame.display.set_caption("AcousticTracing DD")
done = False
clock = pygame.time.Clock()
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 100)
font = pygame.font.Font('freesansbold.ttf', 21)

# create a text suface object,
# on which text is drawn on it.
texto1 = font.render('Imagen a escanear', True, black)
texto2 = font.render('Imagen en proceso', True, black)


# create a rectangular object for the
# text surface object
textRect1 = texto1.get_rect()
textRect2 = texto2.get_rect()


# set the center of the rectangular object.
textRect1.center = (350 , 50)
textRect2.center = (880 , 50)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        # Clear screen to white before drawing
        screen.fill((255, 255, 255))

        # Get a numpy array to display from the simulation

        screen.blit(texto1,textRect1)
        screen.blit(texto2,textRect2)

        modificarPixeles()
        npimage = imagen1
        imagenE = imagen2
        # Convert to a surface and splat onto screen offset by border width and height
        surface = pygame.surfarray.make_surface(npimage)
        screen.blit(surface, (620, 100))

        surface = pygame.surfarray.make_surface(imagenE)
        screen.blit(surface, (100, 100))

        pygame.display.flip()
        clock.tick(60)





