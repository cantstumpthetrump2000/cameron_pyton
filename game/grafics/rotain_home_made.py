import pygame

from math import sin,cos,radians
pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False





pointion1=250,250
distance=20
count=90
angle=radians(90)

orgin=250,250





def distamnce(x,y,x2,y2):
    x_main=x-x2
    y_main=y-y2
    c=x_main**2+y_main**2
    c=c*0.5
    print(c)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        #angle=angle+1
        count=count+1
        if count>360:
            count=0
        angle=radians(count)
        print("current angle",count)


        new_points_x=distance

        new_points_y=distance



        new_points_x_2=(new_points_x*cos(angle)+new_points_y*-sin(angle))



        new_points_y_2=(new_points_x*sin(angle)+new_points_y*(cos(angle)))


        new_points_x_2=new_points_x_2+orgin[0]

        new_points_y_2=new_points_y_2+orgin[1]


        new_points_x_2=new_points_x_2

        new_points_y_2=new_points_y_2


        new_points_x_2=round(new_points_x_2)
        new_points_y_2=round(new_points_y_2)
        print("new pints",new_points_x_2,new_points_y_2)


    #    exit()
        pygame.draw.line(screen, (0, 0, 255), orgin,(new_points_x_2,new_points_y_2),5)
        distamnce(orgin[0],orgin[1],new_points_x_2,new_points_y_2)
        #triangel_points=[]
        #pygame.draw.polygon(screen, (50,50,50), [[100, 100], [100, 400],[400, 300]], 2)



        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 60, 60))
        pygame.display.flip()
        pygame.time.wait(20)
