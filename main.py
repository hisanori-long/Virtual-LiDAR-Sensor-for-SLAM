import env, sensors, robot
import pygame
import math

environment = env.buildEnvironment((520, 950))
environment.originalMap = environment.map.copy()
robot = robot.Robot((200, 100), environment)
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorOn = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys =pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        robot.moveUp()
    elif pressed_keys[pygame.K_s]:
        robot.moveDown()
    elif pressed_keys[pygame.K_a]:
        robot.moveLeft()
    elif pressed_keys[pygame.K_d]:
        robot.moveRight()

    robot_position = robot.getPosition()

    sensor_data = robot.sensingLider()
    environment.dataStorage(sensor_data)
    environment.show_sensorData()
    environment.show_robot(robot_position)
    environment.map.blit(environment.infomap, (0, 0))
