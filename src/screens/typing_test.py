import pygame
import pygame.freetype
import json
import time
import mark_data
import os

white = (255, 255, 255)
gray = (128,128,128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
font_size = 30
num_words = 1
margin = 20

GAME_FONT = pygame.freetype.SysFont("Consolas", font_size)
GAME_FONT.origin = True
space_size = GAME_FONT.get_rect(" ").width
M_ADV_X = 4

class TypingTest:
    def __init__(self, dictionary, change_screen):
        self.crt_char = 0
        self.wrong_char_counter = 0
        self.wrong_char = False
        self.word_dict = dictionary
        self.sentences = self.word_dict.form_sentence(num_words)
        self.blocking_writting = False
        self.change_screen = change_screen
        self.words = self.sentences.split()
        self.mistyped = []
        self.start_time = None
        msg = json.dumps({
            'type': 'start_test',
            'sentence': self.sentences,
            'dictionary': self.word_dict.name
        })
        print(f"msg:{msg}")

    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode == '':
                    # a control key (ctrl, shift, alt, cmd, etc), we ignore them
                    continue

                if self.crt_char == len(self.sentences):
                    # typing test is over
                    # waiting for statistics
                    continue
                
                name_key = ' ' if event.key == pygame.K_SPACE else pygame.key.name(event.key)
                if name_key == "":
                    name_key = event.unicode
                    
                if pygame.K_BACKSPACE == event.key:
                    self.blocking_writting = False
                    continue
                    
                if self.blocking_writting:
                    self.wrong_char = False
                    continue

                elif self.sentences[self.crt_char] == name_key:
                    if self.start_time is None:
                        self.start_time = time.time()
                    self.wrong_char = False
                    self.crt_char += 1
                    if self.crt_char == len(self.sentences):
                        # we ditch logidevmon for now
                        time_elapsed = time.time() - self.start_time
                        wpm = (len(self.sentences) / 5) / (time_elapsed / 60)
                        accuracy = 100 * (1 - self.wrong_char_counter / len(self.sentences))
                        mistyped = self.mistyped
                        statistics_path = os.path.join(
                            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                            "statistics.csv"
                        )
                        mark_data.create_csv_file(statistics_path)
                        mark_data.save_data(statistics_path, [
                            ('wpm', wpm),
                            ('accuracy', accuracy),
                            ('mistyped', mistyped)
                        ])
                        msg = json.dumps({
                            'type': 'end_test',
                            'sentence': self.sentences,
                            'dictionary': self.word_dict.name
                        })
                        print(f"msg:{msg}")

                else:
                    self.wrong_char = True
                    self.blocking_writting = True
                    self.mistyped.append(self.sentences[self.crt_char])
                    self.wrong_char_counter += 1

        surface = pygame.display.get_surface()
        # space_size gets put back by the loop
        line_size = margin - space_size
        y = margin
        words_in_line = []
        sentence_location = 0

        def render_line():
            sentence = " ".join(words_in_line)
            text_surf_rect = GAME_FONT.get_rect(sentence)
            text_surf_rect.topleft = (
                margin,
                y
            )
            baseline = text_surf_rect.y + margin
            metrics = GAME_FONT.get_metrics(sentence)
            x = margin
            for (idx, (char, metric)) in enumerate(zip(sentence, metrics)):
                i = idx + sentence_location

                if i == self.crt_char and self.blocking_writting:
                    GAME_FONT.render_to(surface, (x, baseline), '_' if char == ' ' else char, red)
                elif self.crt_char > i:
                    GAME_FONT.render_to(surface, (x, baseline), char, green)
                else:
                    GAME_FONT.render_to(surface, (x, baseline), char, gray)
                
                x += metric[M_ADV_X]



        for word in self.words:
            rect = GAME_FONT.get_rect(word)
            future_line_size = line_size + space_size + rect.width

            # break line if no space
            if future_line_size + margin*2 >= surface.get_width():
                render_line()
                
                sentence_location += len(" ".join(words_in_line)) + 1
                words_in_line = []
                line_size = margin
                y += margin*2
                future_line_size = line_size + rect.width
            
            line_size = future_line_size
            words_in_line.append(word)
        render_line()