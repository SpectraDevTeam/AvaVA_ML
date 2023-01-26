import pygame
import time
from commands import assistantvoice
from playsound import playsound

num = ''
times = ['minute', 'hours', 'seconds']
def command_matches_input(input):
    if 'timer' in input:
        return True
    else:
        return False

def execute(input):
    num = ''
    for chr in input:
        if chr.isdigit():
    
            num += f'{chr}'
    
    
    for string in times:
        if string in input:

            assistantvoice.speak(f"Timer for {num} {string}s, starting now")
        else:
            assistantvoice.speak(f"Timer for {num} seconds, starting now")

    num = ''
    for chr in input:
        if chr.isdigit():
            
            num += f'{chr}'
    num = int(num)
    if 'minute' in input:
        num *=  60
    if 'hour' in input:
        num *= 60
        num *= 60

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Timer")
    font = pygame.font.SysFont("comicsans", 60)

    start_time = time.time()
    seconds = num

    while seconds >= 0:
        screen.fill((255, 255, 255))
        seconds = num - (time.time() - start_time)
        formatted_time = time.strftime("%M:%S", time.gmtime(seconds))
        text = font.render(formatted_time, True, (0, 0, 0))
        screen.blit(text, (100, 100))
        pygame.display.update()

    playsound('/Users/spectrathefox/Desktop/Repos/SamanthaVA_ML/audiofiles/timerend2.mp3')
    playsound('/Users/spectrathefox/Desktop/Repos/SamanthaVA_ML/audiofiles/timerend2.mp3')
    assistantvoice.speak("Timer is Done")