# Proyecto 2 Analisis de algoritmos
# Daniel Calderon Diaz
# Daniel Villatoro Cantarero

from PIL import Image
import numpy as np
import pygame


#Imagenes del emulador
imagen1 = np.array(Image.open('imagenprueba.jpg'))
imagen2 = np.array(Image.open('imagenprueba.jpg'))



def modificarPixeles():
    for i in range(500):
        for j in range(500):
            if not(np.array_equiv(imagen2[i,j],0)):
                imagen2[i,j] = 88




# --------------------------------------- UI ------------------------------------------------U
h,w=1500,800
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
textRect2.center = (1200 , 50)



# movimiento del radar
x1 = 240
y1 = 240

x2 = 250
y2 = 235

width = 20
height = 20



vel = 10

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    x1, y1 = pygame.mouse.get_pos()
                    print("primero: ",x1, y1)
                    if(x1>950):
                        x1-=950
                    elif(x1<950):
                        x1 = 950 - x1

                    y1-=100
                    x2=x1+10
                    y2=y1-5
                    print(x1, y1)



        screen.fill((255, 255, 255))
        screen.blit(texto1,textRect1)
        screen.blit(texto2,textRect2)

        modificarPixeles()
        imagen1
        imagen2
        # Convert to a surface and splat onto screen offset by border width and height
        surface1 = pygame.surfarray.make_surface(imagen1)
        screen.blit(surface1, (100, 100))


        surface2 = pygame.surfarray.make_surface(imagen2)

        # X  Y W H
        pygame.draw.rect(surface2, (255, 0, 0), (x1, y1, 80, 5))
        pygame.draw.rect(surface2, (255, 255, 255), (x2, y2, 60, 5))

        screen.blit(surface2, (950, 100))

        pygame.display.flip()
        pygame.display.update()





