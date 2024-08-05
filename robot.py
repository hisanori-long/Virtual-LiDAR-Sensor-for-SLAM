import pygame
import sensors

class Robot:

    def __init__(self, startPosition, environment, speed=2):
        self.position = startPosition
        self.environment = environment
        self.speed = speed
        self.lider = sensors.LaserSensor(200, self.environment.originalMap, uncertainty=(0.5, 0.01))

    def getPosition(self):
        return self.position

    def moveUp(self):
        next_position = (self.position[0], self.position[1] - self.speed)
        if self.collision(next_position):
            return
        self.position = next_position
    
    def moveDown(self):
        next_position = (self.position[0], self.position[1] + self.speed)
        if self.collision(next_position):
            return
        self.position = next_position

    def moveLeft(self):
        next_position = (self.position[0] - self.speed, self.position[1])
        if self.collision(next_position):
            return
        self.position = next_position

    def moveRight(self):
        next_position = (self.position[0] + self.speed, self.position[1])
        if self.collision(next_position):
            return
        self.position = next_position

    # 壁に衝突したかどうかを判定
    def collision(self, next_position):
        # 画面外に出た場合　(角の部分に対応するために3の余裕を持たせる)
        if (next_position[0] < 3 or next_position[0] > self.environment.mapw - 3) or (next_position[1] < 3 or next_position[1] > self.environment.maph - 3):
            return True

        # 壁に衝突した場合
        if self.environment.originalMap.get_at(next_position) == (0, 0, 0):
            return True

        return False

    def sensingLider(self):
        self.lider.position = self.position
        sensor_data = self.lider.sense_obstacles()
        return sensor_data
        
