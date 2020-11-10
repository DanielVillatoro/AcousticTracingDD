# Proyecto 2 Analisis de algoritmos
# Daniel Calderon Diaz
# Daniel Villatoro Cantarero

from PIL import Image
from numpy import random
import numpy as np
import pygame
import math

#Imagenes del emulador
imagen1 = np.array(Image.open('imagen.jpg'))
imagen2 = np.array(Image.open('imagen.jpg'))
imagenLogica = np.array(Image.open('imagen.jpg'))

rangoRayos = 15
cantidadRayos = 1500



# def enviarRayos():



def guardarAreaSonar(x,y):
    rangoX, rangoY  = 30,30
    x -= rangoX
    y -= 15
    if (x < rangoX):
        x = 0
    if (y < rangoX):
        y = 0
    area = []
    while(rangoY != 0):
        area += [(x,y)]
        rangoX-=1
        x+=1
        if(rangoX == 0):
            rangoX = 30
            rangoY -= 1
            y += 1
        # imagen2[x,y] = 150
    print("area sonar: ",area)

def calcularXY(x,y):
    if (x > 950):
        x -= 950
    elif (x < 950):
        x = 950 - x
    y -= 100
    # print("Pos sonar:", x, y)
    return (x,y)


def calcularRayo(x,y,angulo):
    x,y = calcularXY(x,y)
    contX = 0 #rango de recorrido x
    contY = 0 #rango de recorrido y
    if angulo == 0:
        for i in range(0,cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, contX, contY, contX)
            enviarRayo(x, y, -contX, contY, contX)
            # for i in range(0,cantidadRayos//2):

    elif angulo == 90 or angulo == -270:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, contX, contY, contY)
            enviarRayo(x, y, contX, -contY, contY)
    elif angulo == -90 or angulo == 270:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, -contX, contY, contY)
            enviarRayo(x, y, -contX, -contY, contY)
    elif angulo == 180 or angulo == -180:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, contX, -contY, contX)
            enviarRayo(x, y, -contX, -contY, contX)



def enviarRayo(x,y,contx,conty,rango):
    if x >= 500 or y >= 500 or x < 0 or y < 0:
        return True
    if rango > rangoRayos:
        return True
    else:
        if not(np.array_equiv(imagenLogica[x,y],0)):
            # imagen2[x][y] = 150
            imagen2[x][y] = calcularEnergía(x,y)
            # print("Pos pixel encontrado: ",x,y)
            return True
        else:
            return enviarRayo(x-contx,y-conty,contx,conty,rango+1)


def calcularEnergía(x2,y2):
    x1 = abs(xSonar-950)
    y1 = abs(ySonar-100)
    energia = 255
    distancia = math.sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    energia =  energia - distancia
    print("Energia:" , energia)
    return energia



def modificarPixeles():
    for i in range(500):
        for j in range(500):
            imagen2[i, j] = 0
            # if not(np.array_equiv(imagen2[i,j],0)):
            #     imagen2[i,j] = 88
            # if i < 100 and j < 100:
            #     imagen2[i, j] = 152


def rotarSonar(imagen,angulo,x,y):
    imagenRotada = pygame.transform.rotozoom(imagen,angulo,1)
    rectRotada = imagenRotada.get_rect(center = (x,y))
    return imagenRotada,rectRotada




# --------------------------------------- GUI ------------------------------------------------U
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
texto1 = font.render('Imagen original', True, black)
texto2 = font.render('Imagen en proceso', True, black)

# create a rectangular object for the
# text surface object
textRect1 = texto1.get_rect()
textRect2 = texto2.get_rect()

# set the center of the rectangular object.
textRect1.center = (350 , 50)
textRect2.center = (1200 , 50)



sonar = pygame.transform.scale(pygame.image.load("sonar.png"),(75,40))
centro = sonar.get_rect()
centro.center = (1190,310)


# movimiento del radar


xSonar = 1190
ySonar = 310


x1 = 240
y1 = 240

x2 = 250
y2 = 235

width = 20
height = 20


angulo = 0

modificarPixeles()

while not done:
        clock.tick(30)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    xSonar, ySonar = pygame.mouse.get_pos()
                    # print("Pos global: ",xSonar, ySonar)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        angulo += 90
                    if event.key == pygame.K_RIGHT:
                        angulo -= 90
                    if event.key == pygame.K_SPACE:
                        # modificarPixeles()
                        calcularRayo(xSonar,ySonar,angulo)
                if event.type == pygame.KEYUP:
                    angulo = angulo
                # print("Angulo: ", angulo)


        if angulo == -360 or angulo == 360:
            angulo = 0
        screen.fill((150, 150, 150))
        screen.blit(texto1,textRect1)
        screen.blit(texto2,textRect2)
        imagen1
        imagen2

        surface1 = pygame.surfarray.make_surface(imagen1)
        screen.blit(surface1, (100, 100))

        surface2 = pygame.surfarray.make_surface(imagen2)
        screen.blit(surface2, (950, 100))

        #rotacion del sonar
        sonarRotado,rotadoRect = rotarSonar(sonar,angulo,xSonar,ySonar)
        screen.blit(sonarRotado,rotadoRect)
        pygame.display.flip()
        pygame.display.update()



