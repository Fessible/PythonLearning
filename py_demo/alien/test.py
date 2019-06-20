import pygame


import sys
screen = pygame.display.set_mode((900,600))
while True:	
    for event in pygame.event.get():		
        if event.type == pygame.QUIT:			
            sys.exit()	
screen.fill((111,111,111))	
pygame.display.flip()