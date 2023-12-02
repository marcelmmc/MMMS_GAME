import pygame

pygame.init()
w = 1280
h = 800
surface = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = True

from screens.typing_test import TypingTest
screen = TypingTest()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    surface.fill("black")
    screen.run(events)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # screen.blit(text, textRect)
    clock.tick(60)  # limits FPS to 60

pygame.quit()