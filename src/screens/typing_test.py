import pygame
from dictionary import Dictionary

white = (255, 255, 255)
gray = (128,128,128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
font_size = 30
num_word_per_sentence = 3
num_sentences = 3

GAME_FONT = pygame.font.SysFont('Helvetica', font_size)

class TypingTest:
    def __init__(self):
        self.crt_char = 0
        self.wrong_char = False
        self.word_dict = Dictionary.load_dictionary('english_5k')
        self.sentences = self.word_dict.form_sentence(num_word_per_sentence*num_sentences)

    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode == '':
                    # a control key (ctrl, shift, alt, cmd, etc), we ignore them
                    continue
                
                if self.sentences[self.crt_char] == pygame.key.name(event.key):
                    self.wrong_char = False
                    self.crt_char += 1

                    if self.crt_char == len(self.sentences):
                        exit(0)
                    elif self.sentences[self.crt_char].isspace():
                        # ignore spaces
                        self.crt_char += 1
                elif pygame.key.name(event.key) == 'space':
                    # ignore spaces
                    continue
                else:
                    self.wrong_char = True

        x = font_size*3
        y = font_size
        spaces = 0

        for i, char in enumerate(self.sentences):
            if spaces == num_word_per_sentence:
                spaces = 0
                x = font_size*3
                y += font_size*4

            if char == ' ':
                x += font_size  # Adjust spacing based on font size
                spaces += 1
                continue 

            # rendered_character = GAME_FONT.render(test_sentence, True, colors[random.randint(0,len(colors)-1)])
            if i == self.crt_char and self.wrong_char:
                rendered_character = GAME_FONT.render(char, True, red)
            elif self.crt_char > i:
                rendered_character = GAME_FONT.render(char, True, green)
            else:
                rendered_character = GAME_FONT.render(char, True, gray)
                
            pygame.display.get_surface().blit(rendered_character, (x, y))
            x += font_size*1  # Adjust spacing based on font size