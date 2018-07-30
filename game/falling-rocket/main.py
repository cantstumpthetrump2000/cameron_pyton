











import pygame



rocket_image="rocket_basic.png"


from PIL import Image
import numpy


im = Image.open(rocket_image)


rocket_image_size=im.size

#landing goals

safe_zone=200



pygame.init()

y_size,x_size=500,500
screen = pygame.display.set_mode((y_size,x_size))
done = False
gravty=0.05
thurst=0.1
clock = pygame.time.Clock()
ground=480
GREEN=(255,0,0)


GAME_MODE="rocket","turret"



def toards_0(x,y):
    if x>0:
        x=x-10
    if x <0:
        x=x+10

    if y>0:
        x=x-10
    if y<0:
        x=x+10
    return(0,0)





class rocket():
    def __init__(self,x_start,y_start):
        self.rocket_iamge=pygame.image.load(rocket_image)
        self.x_posion=x_start
        self.y_posion=y_start

        self.y_speed=0
        self.x_speed=0

    def draw(self):

        screen.blit(self.rocket_iamge,(self.x_posion,self.y_posion))


    def Move_(self,x,y):
        self.y_speed+=y
        self.x_speed+=x

        self.x_posion+=self.x_speed
        self.y_posion+=self.y_speed



class gun():
    def __init__(self,postion):
        self.x,self.y=postion
        self.x_speed,self.y_speed=0,0
        self.size_progectl=5
        self.postion=postion


    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y

    def draw(self):

        pygame.draw.circle(screen, GREEN, (self.x,self.y),self.size_progectl)
        pygame.draw.rect(screen, GREEN, pygame.Rect(self.postion[0],self.postion[1],20,10))

        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(safe_zone,480, 20, 10))





#amin loop

if GAME_MODE=="rocket":
    ship1=rocket(250,250)


if GAME_MODE=="turret":
    startion1=gun((100,100))



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






        if GAME_MODE=="rocket":
            ship1.Move_(0,gravty)


            #ship bonds


            y_bonds_gound=y_size-rocket_image_size[1]
            y_bonds_roff=0

            x_bonds_left=0
            x_bonds_right=x_size-rocket_image_size[0]

            if ship1.y_posion >y_bonds_gound:
                ship1.y_posion=y_bonds_gound

                ship1.x_speed,ship1.y_speed=toards_0(ship1.x_speed,ship1.y_speed)
                if ship1.x_posion>safe_zone and ship1.x_posion<(safe_zone+rocket_image_size[0]+20):
                    print("touch down")
                print("hit the ground ")


            if ship1.y_posion <y_bonds_roff:
                ship1.y_posion=y_bonds_roff

                ship1.x_speed,ship1.y_speed=toards_0(ship1.x_speed,ship1.y_speed)
                print("hit the roff ")


            if ship1.x_posion <x_bonds_left:
                ship1.x_posion=x_bonds_left

                ship1.x_speed,ship1.y_speed=toards_0(ship1.x_speed,ship1.y_speed)
                print("hit the wall left  ")


            if ship1.x_posion >x_bonds_right:
                ship1.x_posion=x_bonds_right

                ship1.x_speed,ship1.y_speed=toards_0(ship1.x_speed,ship1.y_speed)
                print("hit the wall right ")



        startion1.move(1,1)




        screen.fill((255, 255, 255))


        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(safe_zone,480, 20, 10))

        if GAME_MODE=="rocket":
            startion1.draw()

        if GAME_MODE=="rocket":
            ship1.draw()


        pygame.display.flip()
        clock.tick(60)
