import pygame
from dictionary import Dictionary
from typing import List
from screens.typing_test import TypingTest

title_font = pygame.font.SysFont("Helvetica", 50)
selection_font = pygame.font.SysFont("Helvetica", 25)
class TitleScreen:
    def __init__(self, change_screen):
        self.change_screen = change_screen
        self.dictionaries = Dictionary.list_dictionaries()
        self.selected_dictionary = 0

    def run(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            key_name = pygame.key.name(event.key)
            if key_name == "up":
                self.selected_dictionary = (self.selected_dictionary - 1) % len(self.dictionaries)
            elif key_name == "down":
                self.selected_dictionary = (self.selected_dictionary + 1) % len(self.dictionaries)
            elif key_name == "return":
                self.change_screen(
                    TypingTest(
                        Dictionary.load_dictionary(
                            self.dictionaries[self.selected_dictionary]
                        ),
                        self.change_screen
                    )
                )

        surface = pygame.display.get_surface()
        cx = surface.get_width() / 2

        # title
        title = title_font.render("MMMS", True, (255, 255, 255))
        surface.blit(
            title,
            (
                cx - title.get_width()/2,
                100
            )
        )

        dy = 100 + title.get_height() + 20
        for i in range(
            max(0, self.selected_dictionary - 2),
            min(len(self.dictionaries) - 1, self.selected_dictionary + 5) + 1
        ):
            dictionary: str = self.dictionaries[i]
            text = selection_font.render(dictionary, True, (255, 255, 255))
            # 200w50h rect centered
            pygame.draw.rect(
                surface,
                # red if selected, gray if not
                (255, 50, 50) if i == self.selected_dictionary else
                (16, 16, 16),
                pygame.Rect(
                    (
                        cx - 200.0,
                        dy
                    ),
                    (
                        400,
                        50
                    )
                )
            )
            surface.blit(
                text,
                (
                    cx - text.get_width()/2,
                    dy + 25 - text.get_height()/2
                )
            )
            dy += 75

            



        

        