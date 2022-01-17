#This is the main operating file for clicker scape

#Imports
from ssl import Options
import pygame
import time

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
    buttons = {
        'auto_clicker_button' : pygame.Rect(50, 400, 200, 300),
        'clicker_button' : pygame.Rect(350, 250, 100, 100),
        'upgrade_clicker_button' : pygame.Rect(600, 317, 200, 300),
        'double_up_button' : pygame.Rect(278, 571, 148, 20)
        }

    mong = 1
    cost = 50
    cost2 = 50
    cost3 = 500
    game_running = True

    while game_running:
        if game_running:
            autoclick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                print(mopos)

                if(event.button == 1): #Left mouse button
                    for button in buttons:
                        # print(buttons)
                        # print(button)
                        if buttons[button].collidepoint(event.pos):
                            if(button == 'clicker_button'):
                                coins += mong
                                print(button)
                            elif(button == 'upgrade_clicker_button'):
                                if coins >= cost:
                                    coins = coins - cost
                                    cost = cost * 1.5
                                    mong = mong * 1.1
                                    cost = round(cost, 0)
                                print(button)
                            elif(button == 'auto_clicker_button'):
                                if coins >= cost2:
                                    coins = coins - cost2
                                    cost2 = cost2 * 1.5
                                    autog = autog + 0.5
                                    cost2 = round(cost2, 0)
                                print(button)
                            elif(button == 'double_up_button'):
                                if(coins >= cost3):
                                    coins = coins - cost3
                                    cost3 = cost3 * 5
                                    autog = autog * 2
                                    cost3 = round(cost3, 0)
                                print(button)
                            else:
                                print("no button clicked")

                # if mopos >= (350, 0):
                #     if mopos <= (450, 0):
                #         coins += mong

                # if mopos <= (800, 0):
                #     if mopos >= (600, 0):
                #         if coins >= cost:
                #             coins = coins - cost
                #             cost = cost * 1.5
                #             mong = mong * 1.1
                #             cost = round(cost, 0)

                # if mopos >= (50, 0):
                #     if mopos <= (245, 0):
                #         if coins >= cost2:
                #             coins = coins - cost2
                #             cost2 = cost2 * 1.5
                #             autog = autog + 0.5
                #             cost2 = round(cost2, 0)

                #     if mopos >= (278, 542) and mopos <= (424, 561):
                #             print("double up button! A")                        


                if coins == 2147483647:
                    print("You Beat the game!")
                    game_running = False

        #Draw stuff
        gameDisplay.fill(grey)

        for button in buttons:
            if(button == 'clicker_button'):
                print("pain") 
                pygame.draw.rect(gameDisplay,black, buttons[button])
            else:
                pygame.draw.rect(gameDisplay,light_grey, buttons[button])

        DrawText("Clicker Scape", black, white, 400, 100, 50)
        DrawText("You have " + str(f'{coins:.2f}') + " coins", black, white, 100, 50, 20)
        DrawText("Upgrade clicker " + str(cost), black, white, 700, 300, 20)
        DrawText("Buy auto clicker " + str(cost2), black, white, 150, 370, 20)
        DrawText("Double Up! " + str(cost3), black, white, 350, 550, 20)
        DrawText("Version: " + ver, black, white, 650, 50, 20)

        pygame.display.update()
        clock.tick(60)                        

# Ending the program

main_loop()
pygame.quit()
quit()
