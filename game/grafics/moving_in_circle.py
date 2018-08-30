import pygame

from math import sin,cos,radians,atan,degrees,atanh
pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False




while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        points=50,50
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(points[0],points[1], 10, 10))


        pygame.display.flip()
        pygame.time.wait(200)
