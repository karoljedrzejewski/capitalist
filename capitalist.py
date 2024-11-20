import pygame
from player import Player
from UI import draw_text
import programmer
pygame.init()

window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("The Capitalist")
p = Player()
model = pygame.rect.Rect(p.x, p.y, 50, 50)

def main():
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.pay()


        window.fill((20, 100, 200))
        model.x = p.x
        model.y = p.y
        pygame.draw.rect(window, (0, 0, 0), model)
        draw_text(window, f"Balance: {p.balance}$", (50, 50))
        p.move()

        pygame.display.update()

if __name__ == "__main__":
    main()