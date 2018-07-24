import pygame


pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False
gravty=1
thurst=5
clock = pygame.time.Clock()
ground=480

class rocket():
    def __init__(self,x_start,y_start):
        self.rocket_iamge=pygame.image.load("rocket_basic.png")
        self.x_posion=x_start
        self.y_posion=y_start

    def draw(self):
        screen.blit(self.rocket_iamge,(self.x_posion,self.y_posion))
    def Move_(self,x,y):
        self.x_posion+=x
        self.y_posion+=y
#amin loop
ship1=rocket(250,250)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            ship1.Move_(0,-thurst)
        if pressed[pygame.K_a]:
            ship1.Move_(-thurst,0)
        if pressed[pygame.K_s]:
            ship1.Move_(0,thurst)
        if pressed[pygame.K_d]:
            ship1.Move_(thurst,0)



        screen.fill((255, 255, 255))

        ship1.Move_(0,gravty)

        #ship bonds
        y_bonds_gound=480
        y_bonds_roff=20
        x_bonds_left=20
        x_bonds_right=480

        if ship1.y_posion >y_bonds_gound:
            ship1.y_posion=y_bonds_gound
            print("hit the ground ")

        if ship1.y_posion <y_bonds_roff:
            ship1.y_posion=y_bonds_roff
            print("hit the roff ")

        if ship1.x_posion <x_bonds_left:
            ship1.x_posion=x_bonds_left
            print("hit the wall left  ")

        if ship1.x_posion >x_bonds_right:
            ship1.x_posion=x_bonds_right
            print("hit the wall right ")

        ship1.draw()
        pygame.display.flip()
        clock.tick(60)
