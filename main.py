# Proyecto 2 Analisis de algoritmos
# Daniel Calderon Diaz
# Daniel Villatoro Cantarero

from PIL import Image
from numpy import random
import numpy as np
import pygame
import math
import  random
import threading
from datetime import datetime


#Imagenes del emulador
imagen1 = np.array(Image.open('imagen.jpg'))
imagen2 = np.array(Image.open('imagen.jpg'))
imagenLogica = np.array(Image.open('imagen.jpg'))


random.seed(datetime.now())
rangoRayos = 15
cantidadRayos = 600

rangoRayosSecundario = 5
cantidadRayosSecundarios = 50


def calcularXY():
    x = abs(xSonar - 950)
    y = abs(ySonar - 100)
    return (x,y)


def calcularRayo(x,y,angulo,rebote):
    x,y = calcularXY()
    contX = 0 #rango de recorrido x
    contY = 0 #rango de recorrido y
    if angulo == 0:
        for i in range(0,cantidadRayos):
            contX = random.randint(0, rangoRayos)
            contY = random.randint(0, rangoRayos)
            enviarRayo(x, y, contX, contY, contX,1,rebote)
            enviarRayo(x, y, -contX, contY, contX,1,rebote )
            # rayos secundarios
            for i in range(0, cantidadRayosSecundarios ):
                contX = random.randint(0, rangoRayos)
                contY = random.randint(0, rangoRayos)
                enviarRayo(x, y, contX, contY, contX, 2 ,rebote)
                enviarRayo(x, y, -contX, contY, contX, 2,rebote )
    elif angulo == 90 or angulo == -270:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, contX, contY, contY,1,rebote )
            enviarRayo(x, y, contX, -contY, contY,1,rebote )
            # rayos secundarios
            for i in range(0, cantidadRayosSecundarios):
                enviarRayo(x, y, contX, contY, contY, 2 ,rebote)
                enviarRayo(x, y, contX, -contY, contY, 2 ,rebote)
    elif angulo == -90 or angulo == 270:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, -contX, contY, contY,1,rebote)
            enviarRayo(x, y, -contX, -contY, contY,1,rebote )
            # rayos secundarios
            for i in range(0, cantidadRayosSecundarios):
                enviarRayo(x, y, -contX, contY, contY, 2 ,rebote)
                enviarRayo(x, y, -contX, -contY, contY, 2 ,rebote)
    elif angulo == 180 or angulo == -180:
        for i in range(0, cantidadRayos):
            contX = random.randint(1, rangoRayos)
            contY = random.randint(1, rangoRayos)
            enviarRayo(x, y, contX, -contY, contX,1 ,rebote)
            enviarRayo(x, y, -contX, -contY, contX,1 ,rebote)
            # rayos secundarios
            for i in range(0, cantidadRayosSecundarios):
                enviarRayo(x, y, contX, -contY, contX, 2 ,rebote)
                enviarRayo(x, y, -contX, -contY, contX, 2 ,rebote)


def enviarRayo(x,y,contx,conty,rango,tipo,rebote):
    if x >= 500 or y >= 500 or x < 0 or y < 0:
        return True
    if rango > rangoRayos:
        return True
    if tipo == 2 and rango > rangoRayosSecundario:
        return True
    else:
        if not(np.array_equiv(imagenLogica[x,y],0)):
            if tipo == 1:
                if rebote:
                    if angulo == 0:
                        if x > abs(xSonar - 950) or y > abs(ySonar - 100):
                            return True
                        else:
                            imagen2[x][y] = calcularEnergia(x, y)
                            calcularRayo(x, y, 180,True)
                            calcularRayo(x, y, -90, True)
                            calcularRayo(x, y, 90, True)
                    elif angulo == 90 or angulo == -270:
                        if x > abs(xSonar - 950) or y > abs(ySonar - 100):
                            return True
                        else:
                            imagen2[x][y] = calcularEnergia(x, y)
                            calcularRayo(x, y, -90,True)
                            calcularRayo(x, y, 0, True)
                            calcularRayo(x, y, 180, True)
                    elif angulo == -90 or angulo == 270:
                        if x < abs(xSonar - 950) or y < abs(ySonar - 100):
                            return True
                        else:
                            imagen2[x][y] = calcularEnergia(x, y)
                            calcularRayo(x, y, 90,True)
                            calcularRayo(x, y, 0, True)
                            calcularRayo(x, y, 180, True)
                    elif angulo == 180 or angulo == -180:
                        if x < abs(xSonar - 950) or y < abs(ySonar - 100):
                            return True
                        else:
                            imagen2[x][y] = calcularEnergia(x, y)
                            calcularRayo(x, y, 0,True)
                            calcularRayo(x, y, 90, True)
                            calcularRayo(x, y, -90, True)
                else:
                    imagen2[x][y] = calcularEnergia(x, y)
            elif tipo == 2:
                imagen2[x][y] = calcularEnergiaSecundario(x, y)
            return True
        else:
            # if verificarSiguientes(x,y,contx,conty):
            #     return True
            # else:
                return enviarRayo(x-contx,y-conty,contx,conty,rango+1,tipo,rebote)


def verificarSiguientes(x,y,contx,contY):
    cont1 = 1
    cont2 = 1
    cont3 = 0
    if contx < 0:
        cont1 = -1
    if contY < 0:
        cont2 = -1
    contx = abs(contx)
    contY = abs(contY)
    while (cont3 <= contx) :
        x-=cont1
        if not (np.array_equiv(imagenLogica[x, y], 0)):
            return True
        cont3+=1
    cont3 = 0
    while (cont3 <= contY):
        y -= cont2
        if not (np.array_equiv(imagenLogica[x, y], 0)):
            return True
        cont3 += 1
    return False

def calcularEnergiaSecundario(x,y):
    x1 = abs(xSonar - 950)
    y1 = abs(ySonar - 100)
    energia = 255
    distancia = math.sqrt((abs(x1 - x2)) ** 2 + (abs(y1 - y2)) ** 2)
    energia =  energia - distancia
    return energia//2


def calcularEnergia(x2,y2):
    x1 = abs(xSonar-950)
    y1 = abs(ySonar-100)
    energia = 255
    distancia = math.sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    energia =  energia - distancia
    # print("Energia:" , energia)
    return energia



def modificarPixeles():
    for i in range(500):
        for j in range(500):
            imagen2[i, j] = 0



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

        surface1 = pygame.surfarray.make_surface(imagen1)
        surface2 = pygame.surfarray.make_surface(imagen2)

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
                        calcularRayo(xSonar,ySonar,angulo,False)
                        contY = random.randint(1, rangoRayos)
                        print(contY)
                        # pygame.draw.aaline(screen, (255, 0, 0), calcularXY(), (10, 10), 1)
                    if event.key == pygame.K_r:
                        modificarPixeles()
                if event.type == pygame.KEYUP:
                    angulo = angulo
                # print("Angulo: ", angulo)


        if angulo == -360 or angulo == 360:
            angulo = 0

        calcularRayo(xSonar, ySonar, angulo, False)
        screen.fill((150, 150, 150))
        screen.blit(texto1,textRect1)
        screen.blit(texto2,textRect2)
        imagen1
        imagen2

        # pygame.draw.aaline(surface2, (255, 0, 0), calcularXY(), (10, 10), 1)
        screen.blit(surface1, (100, 100))
        screen.blit(surface2, (950, 100))


        #rotacion del sonar
        sonarRotado,rotadoRect = rotarSonar(sonar,angulo,xSonar,ySonar)
        screen.blit(sonarRotado,rotadoRect)
        # pygame.display.flip()
        pygame.display.update()



