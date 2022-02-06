import time, random

# define functions
def autoclick(coins, autog):
    time.sleep(0.1)
    coins = coins + autog
    return coins, autog

def double_boost(autog):
    autog = autog * 2

def generate_nugget(buttons, gameDisplay):
    start = 1
    end = 9696
    x = random.randint(start,end)
    # if x > 8500:
    if x >= 696 and x <= 721:
        print("Ooooh! A Golden Nugget!")
        return True
    return False