import pygame
from threading import Timer

def DrawText(text, Textcolor, Rectcolor, x, y, fsize, gameDisplay):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

def update_elapsed_time(elapsed_time_milli, elapsed_time_sec, elapsed_time_min, elapsed_time_hour, clock):
    elapsed_time_milli = elapsed_time_milli + clock.get_time() # milliseconds
    # print(elapsed_time_milli)

    if(elapsed_time_min > 59):
        elapsed_time_min = 0
        elapsed_time_hour = elapsed_time_hour + 1
    if(elapsed_time_sec > 59):
        elapsed_time_sec = 0
        elapsed_time_min = elapsed_time_min + 1

    if(elapsed_time_milli > 1000):
        # elapsed_time_sec = round(elapsed_time_sec + (elapsed_time_milli / 1000), 0)
        elapsed_time_sec = elapsed_time_sec + (elapsed_time_milli / 1000)
        elapsed_time_sec = int(elapsed_time_sec - (elapsed_time_sec % 1))
        elapsed_time_milli = 0

    return elapsed_time_milli, elapsed_time_sec, elapsed_time_min, elapsed_time_hour

def draw_elapsed_time(elapsed_time_sec, elapsed_time_min, elapsed_time_hour, gameDisplay, colors):
    # black = (0, 0, 0)
    # grey = (128, 128, 128)

    # == == ==
    if(len(str(elapsed_time_sec)) == 1 and len(str(elapsed_time_min)) == 1 and len(str(elapsed_time_hour)) == 1):
        DrawText("0" + str(elapsed_time_hour) + ":0" + str(elapsed_time_min) + ":0" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # == == >
    elif(len(str(elapsed_time_sec)) == 1 and len(str(elapsed_time_min)) == 1 and len(str(elapsed_time_hour)) > 1):
        DrawText(str(elapsed_time_hour) + ":0" + str(elapsed_time_min) + ":0" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # == > >
    elif(len(str(elapsed_time_sec)) == 1 and len(str(elapsed_time_min)) > 1 and len(str(elapsed_time_hour)) > 1):
        DrawText(str(elapsed_time_hour) + ":" + str(elapsed_time_min) + ":0" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # > > >
    elif(len(str(elapsed_time_sec)) > 1 and len(str(elapsed_time_min)) > 1 and len(str(elapsed_time_hour)) > 1):
        DrawText(str(elapsed_time_hour) + ":" + str(elapsed_time_min) + ":" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # > == >
    elif(len(str(elapsed_time_sec)) > 1 and len(str(elapsed_time_min)) == 1 and len(str(elapsed_time_hour)) > 1):
        DrawText(str(elapsed_time_hour) + ":0" + str(elapsed_time_min) + ":" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20), gameDisplay
    # > > ==
    elif(len(str(elapsed_time_sec)) > 1 and len(str(elapsed_time_min)) > 1 and len(str(elapsed_time_hour)) == 1):
        DrawText("0"+ str(elapsed_time_hour) + ":" + str(elapsed_time_min) + ":" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # > == ==
    elif(len(str(elapsed_time_sec)) > 1 and len(str(elapsed_time_min)) == 1 and len(str(elapsed_time_hour)) == 1):
        DrawText("0"+ str(elapsed_time_hour) + ":0" + str(elapsed_time_min) + ":" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)
    # == > ==
    elif(len(str(elapsed_time_sec)) == 1 and len(str(elapsed_time_min)) > 1 and len(str(elapsed_time_hour)) == 1):
        DrawText("0"+ str(elapsed_time_hour) + ":" + str(elapsed_time_min) + ":0" + str(elapsed_time_sec), colors['black'], colors['grey'], 720, 15, 20, gameDisplay)

    # DrawText("Hours: " + str(elapsed_time_hour), black, grey, 720, 15, 20)
    # DrawText("Minutes: " + str(elapsed_time_min), black, grey, 730, 35, 20)
    # DrawText("Seconds: " + str(elapsed_time_sec), black, grey, 730, 55, 20)