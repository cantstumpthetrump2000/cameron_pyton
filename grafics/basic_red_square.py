import pygame

pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False

distance_apart=50
pointion1=250,250
pointion2=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]+(distance_apart/2)
pointion3=pointion1[0]+(distance_apart*(3**0.5)),pointion1[1]-(distance_apart/2)


print("postion of points:")
print(pointion1)
print(pointion2)
print(pointion3)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion1[0],pointion1[1], 5, 5))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion2[1],pointion2[0], 5, 5))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pointion3[1],pointion3[0], 5, 5))


        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 60, 60))
        pygame.display.flip()
