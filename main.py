# Proyecto 2 Analisis de algoritmos
# Daniel Calderon Diaz
# Daniel Villatoro Cantarero

from PIL import Image
import numpy as np
import pygame





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


#Imagenes del emulador
imagen1 = np.array(Image.open('imagenprueba.jpg'))
imagen2 = np.array(Image.open('imagenprueba.jpg'))

sonar = pygame.transform.scale(pygame.image.load("sonar.png"),(75,40))
centro = sonar.get_rect()
centro.center = (1190,310)


# movimiento del radar

def rotarSonar(imagen,angulo,x,y):
    imagenRotada = pygame.transform.rotozoom(imagen,angulo,1)
    rectRotada = imagenRotada.get_rect(center = (x,y))
    return imagenRotada,rectRotada



xSonar = 1190
ySonar = 310


x1 = 240
y1 = 240

x2 = 250
y2 = 235

width = 20
height = 20


angulo = 0

while not done:
        clock.tick(30)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    xSonar, ySonar = pygame.mouse.get_pos()
                    # print("primero: ",xSonar, ySonar)
                    # if(xSonar>950):
                    #     xSonar-=950
                    # elif(xSonar<950):
                    #     xSonar = 950 - xSonar
                    #
                    # ySonar-=100
                    # x2=xSonar+10
                    # y2=ySonar-5
                    # print(xSonar, ySonar)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        angulo += 10
                    if event.key == pygame.K_RIGHT:
                        angulo -= 10
                if event.type == pygame.KEYUP:
                    angulo = angulo

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
        screen.blit(surface2, (950, 100))


        #rotacion del sonar

        sonarRotado,rotadoRect = rotarSonar(sonar,angulo,xSonar,ySonar)
        screen.blit(sonarRotado,rotadoRect)

        pygame.display.flip()
        pygame.display.update()





