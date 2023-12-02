import pygame

white = (255, 255, 255)
gray = (128,128,128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
font_size = 30
num_word_per_sentence = 4
num_sentences = 6

GAME_FONT = pygame.font.SysFont('Helvetica', font_size)

class TypingTest:
    def __init__(self, dictionary, change_screen):
        self.crt_char = 0
        self.wrong_char = False
        self.word_dict = dictionary
        self.sentences = self.word_dict.form_sentence(num_word_per_sentence*num_sentences)
        self.blocking_writting = False
        self.change_screen = change_screen

    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode == '':
                    # a control key (ctrl, shift, alt, cmd, etc), we ignore them
                    continue
                
                name_key = ' ' if event.key == pygame.K_SPACE else pygame.key.name(event.key)
                if name_key == "":
                    name_key = event.unicode
                    
                if self.blocking_writting:
                    self.blocking_writting = not pygame.K_BACKSPACE == event.key

                elif self.sentences[self.crt_char] == name_key:
                    self.wrong_char = False
                    self.crt_char += 1
                    if self.crt_char == len(self.sentences):
                        exit(0)
                        
                else:
                    self.wrong_char = True
                    self.blocking_writting = True

        x = font_size*3
        y = font_size
        spaces = 0

        for i, char in enumerate(self.sentences):
            if spaces == num_word_per_sentence:
                spaces = 0
                x = font_size*3
                y += font_size*3

            if char == ' ':
                spaces += 1

            # rendered_character = GAME_FONT.render(test_sentence, True, colors[random.randint(0,len(colors)-1)])
            if i == self.crt_char and self.blocking_writting:
                rendered_character = GAME_FONT.render('_' if char == ' ' else char, True, red)
            elif self.crt_char > i:
                rendered_character = GAME_FONT.render(char, True, green)
            else:
                rendered_character = GAME_FONT.render(char, True, gray)
                
            pygame.display.get_surface().blit(rendered_character, (x, y))
            x += font_size*1  # Adjust spacing based on font size