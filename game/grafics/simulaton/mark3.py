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
    return(c/100)

distance_apart=50
count=0



pointion1=250,250

pointion2=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]+(distance_apart/2)

pointion3=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]-(distance_apart/2)


orgin=pointion1[0],pointion1[1]+((distance_apart*(3**0.5))/2)
print("orgin",orgin)

#offset1=orgin[0]-pointion1[0],orgin[1]-pointion1[1]
#offset2=orgin[0]-pointion2[0],orgin[1]-pointion2[1]
#offset3=orgin[0]-pointion3[0],orgin[1]-pointion3[1]

offset1=[0.0,43.3]
offset2=[86.6,18.3]
offset3=[-86.6,-68.3]

print("offsets")

print(offset1)
print(offset2)
print(offset3)

new_point=orgin



while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        point_to_point_at=pygame.mouse.get_pos()
        offset1=[0.0,-43.3]
        offset2=[86.6,18.3]
        offset3=[-86.6,-68.3]
        new_point=orgin




        #new_point
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pointion1[1],pointion1[0], 10, 10))
        mod1=distamnce_calutor(pointion1[1],pointion1[0],point_to_point_at[1],point_to_point_at[0])
        offset1[0]=offset1[0]*mod1
        offset1[1]=offset1[1]*mod1


        new_point=new_point[0]+offset1[0],new_point[1]+offset1[1]




        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pointion2[1],pointion2[0], 10, 10))
        mod2=distamnce_calutor(pointion1[1],pointion1[0],point_to_point_at[1],point_to_point_at[0])
        offset2[0]=offset2[0]*mod2
        offset2[1]=offset2[1]*mod2

        new_point=new_point[0]+offset2[0],new_point[1]+offset2[1]

        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(pointion3[1],pointion3[0], 10, 10))
        mod3=distamnce_calutor(pointion1[1],pointion1[0],point_to_point_at[1],point_to_point_at[0])


        offset3[0]=offset3[0]*mod3
        offset3[1]=offset3[1]*mod3
        new_point=new_point[0]+offset3[0],new_point[1]+offset3[1]


        pygame.draw.line(screen, (0, 0, 0), orgin,new_point,5)

        pygame.display.flip()
        pygame.time.wait(200)
