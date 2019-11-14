import pygame

from scene_base import SceneBase
from game_scene import GameScene

class TitleScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsansms", 45)
        text = font.render("Snake (AI?)", True, (0, 0, 0))
        screen.blit(text, (100, 75))
