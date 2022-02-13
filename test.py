import pygame
pygame.init()
while True:
    disp=pygame.display.set_mode((1000,500))
    pygame.draw.circle(disp,(255,100,2),(400,200),30,10)
    pygame.draw.circle(disp,(255,100,2),(550,200),30,10)
    pygame.draw.rect(disp,(255,150,10),(420,350,100,10),2)
    pygame.display.update()