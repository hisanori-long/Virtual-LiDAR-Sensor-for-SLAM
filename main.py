import env, sensors
import pygame
import math

environment = env.buildEnvironment((550, 950))
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
