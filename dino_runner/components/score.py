import pygame

from dino_runner.utils.constants import FONT_STYLE

class Score:

    MAX_SCORE = 0
    def __init__(self):
        self.max_score = self.MAX_SCORE
        self.score = 0
            
    def update_score(self, game):
        self.score += 1
        
        if self.score % 100 == 0 and game.game_speed < 500:
            game.game_speed += 2
        elif self.score > self.max_score:
            self.max_score = self.score

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0) )
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)
    


