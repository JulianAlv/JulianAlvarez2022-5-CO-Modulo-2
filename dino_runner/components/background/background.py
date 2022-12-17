import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Background(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, 240)

    def update(self, game_speed, background):
        self.rect.x -= game_speed

        if self.rect.x < - self.rect.width:
            background.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))