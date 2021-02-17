#Reference:
#https://www.edureka.co/blog/snake-game-with-pygame/#install
#https://www.pygame.org/docs/tut/PygameIntro.html

import pygame
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game')
game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		print(event) #prints out all the actions that take place on the screen

pygame.quit()
quit()












