import pygame 
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
  
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.text = self.font.render(message, True, (0, 0, 0,))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
    
    def handle_events_on_menu(self, game):
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif even.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen_color(seld, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0,))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)