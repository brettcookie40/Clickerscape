#This is the main operating file for clicker scape

#Imports
from ssl import Options
from threading import Timer
import pygame, time, random

#Initialize pygame
pygame.init()

#defining variables
clock = pygame.time.Clock()
ver = "0.0.0"
autog = 0
coins = 0
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
yellow = ((255,255,0))
moon_glow = ((235,245,255))

# creating display and caption
gameDisplay = pygame.display.set_mode((display_width, display_height));
pygame.display.set_caption("ClickerScape");

# define functions
def autoclick():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog

def double_boost(autog):
    autog = autog * 2;

def generate_nugget(buttons, gameDisplay):
    start = 1
    end = 9696
    x = random.randint(start,end)
    # if x > 8500:
    if x >= 696 and x <= 721:
        print("Ooooh! A Golden Nugget!")
        return True
    return False
        

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

def main_loop():
    #The goods
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3   
    global coins
    gameDisplay.fill(grey)
    dt = clock.get_time() #keeping track of time between previous tick check
    buttons = {
        'auto_clicker_button' : pygame.Rect(50, 400, 200, 300),
        'clicker_button' : pygame.Rect(350, 250, 100, 100),
        'upgrade_clicker_button' : pygame.Rect(550, 317, 200, 300),
        'double_up_button' : pygame.Rect(327, 571, 148, 20),
        'golden_nugget' : pygame.Rect(130, 200, 50, 50)
        }
    
    is_showing_nugget = False
    mong = 1
    cost = 10
    cost2 = 25
    cost3 = 500
    elapsed_time_milli = 0
    elapsed_time_sec = 0
    elapsed_time_min = 0
    elapsed_time_hour = 0
    game_running = True
    # rt = RepeatedTimer(1, generate_nugget, buttons, gameDisplay)

    while game_running:
        elapsed_time_milli = elapsed_time_milli + clock.get_time() # milliseconds
        # print(elapsed_time_milli)

        if(elapsed_time_min > 59):
            elapsed_time_min = 0
            elapsed_time_hour = elapsed_time_hour + 1
        if(elapsed_time_sec > 59):
            elapsed_time_sec = 0
            elapsed_time_min = elapsed_time_min + 1

        if(elapsed_time_milli > 1000):
            elapsed_time_sec = round(elapsed_time_sec + (elapsed_time_milli / 1000), 0)
            elapsed_time_milli = 0

        #golden nuggets
        if(is_showing_nugget == True):
            dt = dt + clock.get_time()
            if(dt > 10000): #Remove nugget after 10 seconds
                print("You were too slow!")
                is_showing_nugget = False
                gameDisplay.fill(grey)
                dt = 0
        else:
            dt = dt + clock.get_time()
            if(dt > 1000):
                is_showing_nugget = generate_nugget(buttons, gameDisplay)
                dt = 0

        if game_running:
            autoclick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                # print(mopos)

                if(event.button == 1): #Left mouse button
                    for button in buttons:
                        if buttons[button].collidepoint(event.pos):
                            if(button == 'clicker_button'):
                                coins += mong
                                # print(button)
                            elif(button == 'upgrade_clicker_button'):
                                if coins >= cost:
                                    coins = coins - cost
                                    cost = cost * 1.75
                                    mong = mong * 1.5
                                    cost = round(cost, 0)
                                # print(button)
                            elif(button == 'auto_clicker_button'):
                                if coins >= cost2:
                                    coins = coins - cost2
                                    cost2 = cost2 * 1.5
                                    autog = autog + 0.5
                                    cost2 = round(cost2, 0)
                                # print(button)
                            elif(button == 'double_up_button'):
                                if(coins >= cost3):
                                    if(autog == 0): #If user hasn't purchased auto clicker, activate their autoclicker at 1*2 speed
                                        coins = coins - cost3
                                        cost3 = cost3 * 5
                                        autog = (autog + 1) * 2
                                        cost3 = round(cost3, 0)
                                    else:        
                                        coins = coins - cost3
                                        cost3 = cost3 * 5
                                        autog = autog * 2
                                        cost3 = round(cost3, 0)
                                # print(button)
                            elif(button == 'golden_nugget' and is_showing_nugget == True):
                                coins += 30000 + round((coins * .2), 0)
                                is_showing_nugget = False
                                gameDisplay.fill(grey)
                            else:
                                #For now
                                pass
                            

                if coins >= 112147483647:
                    print("You Beat the game!")
                    game_running = False

        gameDisplay.fill(grey)

        #Draw stuff
        for button in buttons:
            if(button == 'clicker_button'):
                pygame.draw.rect(gameDisplay, moon_glow, buttons[button])

            elif(button != 'golden_nugget'):
                pygame.draw.rect(gameDisplay, black, buttons[button])

            if (button == 'golden_nugget' and is_showing_nugget == True):
                pygame.draw.rect(gameDisplay, yellow, buttons[button])

        DrawText("Clicker Scape", black, white, 400, 100, 50)
        DrawText("Upgrade Clicker " + str(cost), black, white, 650, 270, 20)
        DrawText("Buy Auto Clicker " + str(cost2), black, white, 150, 350, 20)
        DrawText("Double Up Multiplier! " + str(cost3), black, white, 400, 550, 20)
        DrawText("Version: " + ver, black, white, 650, 50, 20)
        DrawText("Hours: " + str(elapsed_time_hour) + " Minutes: " + str(elapsed_time_min) + " Seconds: " + str(elapsed_time_sec), black, white, 620, 140, 20)
        DrawText("Auto Click Multiplier: " + str(autog), black, white, 150, 370, 20)
        DrawText("Clicker Value: " + str(round(mong, 2)), black, white, 650, 290, 20)
        

        if(coins < 50000):
            DrawText("You have " + str(f'{coins:.2f}') + " coins ", black, white, 150, 50, 20)
        elif(coins >= 50000 and coins < 300000):
            DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", black, white, 150, 50, 20)
        elif(coins >= 300000 and coins < 1000000):
            DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", black, white, 150, 50, 20)
            DrawText("Keep Dreamin'!", black, white, 150, 70, 15 )
        elif(coins >= 1000000 and coins < 1000000000):
            DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", black, white, 150, 50, 20)
            DrawText("Woo Millionaire!!!", black, white, 150, 70, 15 )
        elif(coins >= 1000000000 and coins < 1000000000000):
            DrawText("OMG Billionaire!!!@##$%&$%#@", black, white, 150, 70, 15 )
        pygame.display.update()
        clock.tick(60)                        

# Ending the program
main_loop()
pygame.quit()
quit()
