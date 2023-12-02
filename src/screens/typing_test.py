import pygame
import pygame.freetype

white = (255, 255, 255)
gray = (128,128,128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
font_size = 30
num_word_per_sentence = 10
num_sentences = 6
margin = 20

GAME_FONT = pygame.freetype.Font(None, font_size)
GAME_FONT.origin = True
space_size = GAME_FONT.get_rect(" ").width
M_ADV_X = 4

class TypingTest:
    def __init__(self, dictionary, change_screen):
        self.crt_char = 0
        self.wrong_char = False
        self.word_dict = dictionary
        self.sentences = self.word_dict.form_sentence(num_word_per_sentence*num_sentences)
        self.blocking_writting = False
        self.change_screen = change_screen
        self.words = self.sentences.split()
        print(self.words, self.sentences)

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

        surface = pygame.display.get_surface()
        # space_size gets put back by the loop
        line_size = margin - space_size
        y = margin
        words_in_line = []
        sentence_location = 0

        def render_line():
            sentence = " ".join(words_in_line)
            text_surf_rect = GAME_FONT.get_rect(sentence)
            text_surf = pygame.Surface(text_surf_rect.size)
            text_surf_rect.topleft = (
                margin,
                y
            )
            baseline = text_surf_rect.y
            metrics = GAME_FONT.get_metrics(sentence)
            x = 0
            for (idx, (char, metric)) in enumerate(zip(sentence, metrics)):
                i = idx + sentence_location
                # rendered_character = GAME_FONT.render(test_sentence, True, colors[random.randint(0,len(colors)-1)])
                if i == self.crt_char and self.blocking_writting:
                    GAME_FONT.render_to(text_surf, (x, baseline), '_' if char == ' ' else char, red)
                elif self.crt_char > i:
                    GAME_FONT.render_to(text_surf, (x, baseline), char, green)
                else:
                    GAME_FONT.render_to(text_surf, (x, baseline), char, gray)
                
                x += metric[M_ADV_X]

            surface.blit(text_surf, text_surf_rect)


        for word in self.words:
            rect = GAME_FONT.get_rect(word)
            future_line_size = line_size + space_size + rect.width

            # break line if no space
            if future_line_size + margin > surface.get_width():
                render_line()
                
                sentence_location += len(" ".join(words_in_line)) + 1
                words_in_line = []
                line_size = margin
                y += margin
                future_line_size = line_size + rect.width
            
            line_size = future_line_size
            words_in_line.append(word)
        render_line()