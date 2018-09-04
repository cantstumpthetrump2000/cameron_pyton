import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('teaxt demo')
clock = pygame.time.Clock()




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,postion):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (postion)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()








gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




    gameDisplay.fill(white)


    message_display('You Crashed',(0,0))
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
