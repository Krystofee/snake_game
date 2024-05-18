import pygame
from constants import SNAKE_BLOCK_SIZE, INITIAL_SNAKE_LENGTH, SCREEN_SIZE
import random

class Snake:
    def __init__(self):
        self.length = INITIAL_SNAKE_LENGTH
        self.positions = [((SCREEN_SIZE[0] // 2), (SCREEN_SIZE[1] // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.grow = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if len(self.positions) > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * SNAKE_BLOCK_SIZE)) % SCREEN_SIZE[0]), (cur[1] + (y * SNAKE_BLOCK_SIZE)) % SCREEN_SIZE[1])
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if self.grow:
                self.grow = False
            else:
                self.positions.pop()

    def reset(self):
        self.length = INITIAL_SNAKE_LENGTH
        self.positions = [((SCREEN_SIZE[0] // 2), (SCREEN_SIZE[1] // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def check_collision(self):
        if self.positions[0] in self.positions[1:]:
            return True
        return False

    def render(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE))
            pygame.draw.rect(surface, (0, 255, 0), rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)

    def handle_keys(self, event):
        if event.key == pygame.K_UP:
            self.turn((0, -1))
        elif event.key == pygame.K_DOWN:
            self.turn((0, 1))
        elif event.key == pygame.K_LEFT:
            self.turn((-1, 0))
        elif event.key == pygame.K_RIGHT:
            self.turn((1, 0))

    def grow_snake(self):
        self.grow = True
