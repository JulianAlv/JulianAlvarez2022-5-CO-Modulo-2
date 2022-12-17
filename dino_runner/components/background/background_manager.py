
from dino_runner.components.background.cloud import Cloud


class Background_Manager:
    def __init__(self):
        self.backgrounds = []

    def update(self, game):
        self.generate_cloud()
        for background in self.backgrounds:
            background.update(game.game_speed, self.backgrounds)
    
    def draw(self, screen):
        for background in self.backgrounds:
            background.draw(screen)

    def generate_cloud(self):
        if len(self.backgrounds) == 0:
            self.backgrounds.append(Cloud())

    def reset_cloud(self):
        self.backgrounds = []