#Reference:
#https://www.edureka.co/blog/snake-game-with-pygame/#install
#https://www.pygame.org/docs/tut/PygameIntro.html

import pygame
pygame.init()
dis = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Snake game')

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		# print(event) #prints out all the actions that take place on the screen

	pygame.draw.rect(dis, green, [200, 150, 10, 10])
	pygame.display.update()

pygame.quit()
quit()












