#This is the main operating file for clicker scape

#Imports
from ssl import Options
from threading import Timer
import pygame, time, random
import pygame_menu
import calc_funcs, draw_funcs

#Initialize pygame
pygame.init()

#defining variables
clock = pygame.time.Clock()
ver = "0.0.1"
autog = 0
coins = 0
display_width = 800
display_height = 600

colors = {
    'white': (255,255,255),
    'black': (0,0,0),
    'grey': (128,128,128),
    'light_grey': (224,224,224),
    'yellow': (255,255,0),
    'gold': ((255,204,0)),
    'moon_glow': ((235,245,255)),
}

# creating display and caption
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ClickerScape")

def main_loop():
    #The goods
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3   
    global coins
    clicker_color = colors['moon_glow']
    gameDisplay.fill(colors['grey'])
    dt = clock.get_time() #keeping track of time between previous tick check
    buttons = {
        'auto_clicker_button' : pygame.Rect(50, 400, 200, 300),
        'clicker_button' : pygame.Rect(350, 250, 100, 100),
        'upgrade_clicker_button' : pygame.Rect(550, 317, 200, 300),
        'double_up_button' : pygame.Rect(327, 571, 148, 20),
        'golden_nugget' : pygame.Rect(130, 200, 50, 50),
        'skills_button': pygame.Rect(10, 60, 120, 30),
        }
    coin_text_info = {
        'x-coord': 400,
        'y-coord': 50,
        'height': 20,
    }
    game_running = True
    is_showing_nugget = False
    mong = 1
    cost = 10
    cost2 = 25
    cost3 = 500
    elapsed_time_milli = 0
    elapsed_time_sec = 0
    elapsed_time_min = 0
    elapsed_time_hour = 0
    
    # rt = RepeatedTimer(1, generate_nugget, buttons, gameDisplay)

    while game_running:
        #updating time values
        elapsed_time_milli, elapsed_time_sec, elapsed_time_min, elapsed_time_hour = draw_funcs.update_elapsed_time(elapsed_time_milli, elapsed_time_sec, elapsed_time_min, elapsed_time_hour, clock)

        #golden nuggets
        if(is_showing_nugget == True):
            dt = dt + clock.get_time()
            if(dt > 10000): #Remove nugget after 10 seconds
                print("You were too slow!")
                is_showing_nugget = False
                gameDisplay.fill(colors['grey'])
                dt = 0
        else:
            dt = dt + clock.get_time()
            if(dt > 1000):
                is_showing_nugget = calc_funcs.generate_nugget(buttons, gameDisplay)
                dt = 0

        if game_running:
            coins, autog = calc_funcs.autoclick(coins, autog)
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
                                clicker_color = ((random.randint(0, 255) , random.randint(0, 255), random.randint(0, 255)))
                                # print(button)
                            elif(button == 'upgrade_clicker_button'):
                                if coins >= cost:
                                    coins = coins - cost
                                    cost = cost * 2.5
                                    mong = mong * 2
                                    cost = round(cost, 0)
                                # print(button)
                            elif(button == 'auto_clicker_button'):
                                if coins >= cost2:
                                    if(autog == 0):
                                        coins = coins - cost2
                                        cost2 = cost2 * 1.75
                                        autog = autog + 0.5
                                        cost2 = round(cost2, 0)
                                    else:    
                                        coins = coins - cost2
                                        cost2 = cost2 * 1.85
                                        autog = round(autog + (autog * 0.30),2)
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
                                gameDisplay.fill(colors['grey'])
                            else:
                                #For now
                                pass
                            

                if coins >= 112147483647:
                    print("You Beat the game!")
                    game_running = False

        gameDisplay.fill(colors['grey'])

        #Draw stuff
        for button in buttons:
            if(button == 'clicker_button'):
                pygame.draw.rect(gameDisplay, clicker_color, buttons[button])

            elif(button != 'golden_nugget'):
                if(button == 'skills_button'):
                    pygame.draw.rect(gameDisplay, colors['black'], buttons[button], 2)
                else:
                    pygame.draw.rect(gameDisplay, colors['black'], buttons[button])

            if (button == 'golden_nugget' and is_showing_nugget == True):
                pygame.draw.rect(gameDisplay, colors['yellow'], buttons[button])

        # DrawText("Clicker Scape", black, grey, 400, 100, 50)
        draw_funcs.DrawText("Upgrade Clicker " + str(cost), colors['black'], colors['grey'], 650, 270, 20, gameDisplay)
        draw_funcs.DrawText("Buy Auto Clicker " + str(cost2), colors['black'], colors['grey'], 150, 350, 20, gameDisplay)
        draw_funcs.DrawText("Double Up Multiplier! " + str(cost3), colors['black'], colors['grey'], 400, 550, 20, gameDisplay)
        draw_funcs.DrawText("Version: " + ver, colors['black'], colors['grey'], 35, 5, 10, gameDisplay)
        draw_funcs.DrawText("Skills", colors['gold'], colors['grey'], 70, 75, 25, gameDisplay) #10, 60 120, 30
        draw_funcs.draw_elapsed_time(elapsed_time_sec, elapsed_time_min, elapsed_time_hour, gameDisplay, colors)

        draw_funcs.DrawText("Auto Click Value: " + str(autog), colors['black'], colors['grey'], 150, 370, 20, gameDisplay)
        draw_funcs.DrawText("Clicker Value: " + str(round(mong, 2)), colors['black'], colors['grey'], 650, 290, 20, gameDisplay)
        

        if(coins < 50000):
            draw_funcs.DrawText("You have " + str(f'{coins:.2f}') + " coins ", colors['gold'],  colors['grey'], coin_text_info['x-coord'], coin_text_info['y-coord'], coin_text_info['height'], gameDisplay)
        elif(coins >= 50000 and coins < 300000):
            draw_funcs.DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", colors['gold'],  colors['grey'], coin_text_info['x-coord'], coin_text_info['y-coord'], coin_text_info['height'], gameDisplay)
        elif(coins >= 300000 and coins < 1000000):
            draw_funcs.DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", colors['gold'],  colors['grey'], coin_text_info['x-coord'], coin_text_info['y-coord'], coin_text_info['height'], gameDisplay)
            draw_funcs.DrawText("Keep Dreamin'!", colors['gold'], colors['grey'], coin_text_info['x-coord'], (coin_text_info['y-coord'] + coin_text_info['height']), 15, gameDisplay)
        elif(coins >= 1000000 and coins < 1000000000):
            draw_funcs.DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", colors['gold'],  colors['grey'], coin_text_info['x-coord'], coin_text_info['y-coord'], coin_text_info['height'], gameDisplay)
            draw_funcs.DrawText("Woo Millionaire!!!", colors['gold'], colors['grey'], coin_text_info['x-coord'], (coin_text_info['y-coord'] + coin_text_info['height']), 15, gameDisplay)
        elif(coins >= 1000000000 and coins < 1000000000000):
            draw_funcs.DrawText("You have " + str(f'{coins:.2f}') + " coins!!!", colors['gold'],  colors['grey'], coin_text_info['x-coord'], coin_text_info['y-coord'], coin_text_info['height'], gameDisplay)
            draw_funcs.DrawText("OMG Billionaire!!!@##$%&$%#@", colors['gold'], colors['grey'], coin_text_info['x-coord'], (coin_text_info['y-coord'] + coin_text_info['height']), 15, gameDisplay)
        pygame.display.update()
        clock.tick(60)

# Ending the program
main_loop()
pygame.quit()
quit()
