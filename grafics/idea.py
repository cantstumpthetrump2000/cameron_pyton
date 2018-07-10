import pygame

from math import sin,cos,radians,atan,degrees,atanh
pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False





point_to_point_at=pygame.mouse.get_pos()




def distamnce(x,y,x2,y2):
    x_main=x-x2
    y_main=y-y2
    c=x_main**2+y_main**2
    c=c*0.5
    print(c)

distance_apart=50
count=0
distance=20
pointion1=250,250
pointion2=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]+(distance_apart/2)
pointion3=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]-(distance_apart/2)



orgin=pointion1[0],pointion1[1]+((distance_apart*(3**0.5))/2)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        #angle=angle+1



        point_to_point_at=pygame.mouse.get_pos()



        pygame.draw.line(screen, (0, 0, 255), orgin,(point_to_point_at[0],point_to_point_at[1]),5)


        pygame.display.flip()
        pygame.time.wait(20)
