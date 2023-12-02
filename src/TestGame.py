import pygame
import random
from dictionary import Dictionary

pygame.init()
w = 1280
h = 800
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = True
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
gray = (128,128,128)
font_size = 30
colors = [white, green, blue]

GAME_FONT = pygame.font.SysFont('Helvetica', font_size)
word_dict = Dictionary.load_dictionary('english_5k')
num_word_per_sentece = 3
num_sentences = 3
sentences =  word_dict.form_sentence(num_word_per_sentece*num_sentences)
print(sentences)

crt_char = 0
screen.fill("black")
wrong_char = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if crt_char >= len(sentences):
                print('change to winning screen')
            elif sentences[crt_char] == pygame.key.name(event.key):
                wrong_char = False
                crt_char = crt_char + 1 if crt_char < len(sentences) and not sentences[crt_char + 1].isspace() else crt_char + 2
            else: 
                wrong_char = True
            
        if event.type == pygame.QUIT:
            running = False


    x = font_size*3
    y = font_size
    spaces = 0
    for i, char in enumerate(sentences):

        if spaces == num_word_per_sentece:
            spaces = 0
            x = font_size*3
            y += font_size*4

        if char == ' ':
            x += font_size  # Adjust spacing based on font size
            spaces += 1
            continue 

        # rendered_character = GAME_FONT.render(test_sentence, True, colors[random.randint(0,len(colors)-1)])
        if i == crt_char and wrong_char:
            rendered_character = GAME_FONT.render(char, True, red)
        elif crt_char > i:
            rendered_character = GAME_FONT.render(char, True, green)
        else:
            rendered_character = GAME_FONT.render(char, True, gray)
            
        screen.blit(rendered_character, (x, y))
        x += font_size*1  # Adjust spacing based on font size


    # flip() the display to put your work on screen
    pygame.display.flip()
    # screen.blit(text, textRect)
    clock.tick(60)  # limits FPS to 60

pygame.quit()