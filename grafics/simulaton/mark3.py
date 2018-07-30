import pygame

from math import sin,cos,radians,atan,degrees,atanh
pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False









def distamnce_calutor(x,y,x2,y2):
    x_main=x-x2
    y_main=y-y2
    c=x_main**2+y_main**2
    c=c**0.5
    return(c)

distance_apart=50
count=0



pointion1=250,250



pointion2=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]+(distance_apart/2)


pointion3=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]-(distance_apart/2)


#orgin=pointion1[0],pointion1[1]+((distance_apart*(3**0.5))/2)





while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        point_to_point_at=pygame.mouse.get_pos()

    #    pygame.draw.line(screen, (0, 0, 255), orgin,(direction),5)

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pointion1[1],pointion1[0], 10, 10))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pointion2[1],pointion2[0], 10, 10))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(pointion3[1],pointion3[0], 10, 10))





        pygame.display.flip()
        pygame.time.wait(200)
