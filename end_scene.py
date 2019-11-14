import pygame

from scene_base import SceneBase

class EndScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
            
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsansms", 150)
        text = font.render("LOL", True, (0, 0, 0))
        screen.blit(text, (100, 120))
