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
        point_to_point_at=pygame.mouse.get_pos()



    #    pygame.draw.line(screen, (0, 0, 255), orgin,(new_points_x_2,new_points_y_2),5)
        #print(pointion1[0])
        #print(type(point_to_point_at[0]))
        #print(pointion1[1])
        #print(point_to_point_at[1])
        distance_from_pool_1=distamnce_calutor(pointion1[1],pointion1[0],point_to_point_at[0],point_to_point_at[1])
        distance_from_pool_2=distamnce_calutor(pointion2[1],pointion2[0],point_to_point_at[0],point_to_point_at[1])
        distance_from_pool_3=distamnce_calutor(pointion3[1],pointion3[0],point_to_point_at[0],point_to_point_at[1])



        #print("distasnces:")
        #print(distance_from_pool_1)
        #print(distance_from_pool_2)
        #print(distance_from_pool_3)

        offset_of_points_1=0,((distance_apart*(3**0.5))/2)

        offset_of_points_2=(distance_apart*(3**0.5)),((distance_apart*(3**0.5))/2)
        offset_of_points_3=(distance_apart*(3**0.5)),(-(distance_apart*(3**0.5))/2)


        print(offset_of_points_1)
        print(offset_of_points_2)
        print(offset_of_points_3)
    #    exit()
        direction=orgin[1],orgin[0]
        direction=direction[1]+(offset_of_points_1[0]*distance_from_pool_1),direction[0]+(offset_of_points_1[1]*distance_from_pool_1)
        direction=direction[1]+(offset_of_points_2[0]*distance_from_pool_2),direction[0]+(offset_of_points_2[1]*distance_from_pool_2)
        direction=direction[1]+(offset_of_points_3[0]*distance_from_pool_3),direction[0]+(offset_of_points_3[1]*distance_from_pool_3)

        print(direction)
        pygame.draw.line(screen, (0, 0, 255), orgin,(direction),5)

        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion1[1],pointion1[0], 5, 5))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion2[1],pointion2[0], 10, 10))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion3[1],pointion3[0], 15, 15))





        pygame.display.flip()
        pygame.time.wait(200)
