import pygame

def draw_text(surface, text, pos, size=36, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)