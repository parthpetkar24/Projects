#-----------------------------------------Rock, Paper and Scissors Game-----------------------------------

# Random module to select rock, paper or scissors randomly
import random
from time import sleep

#Total points of player
points=0

# List containing Playable contents 
options=["Rock","Scissors","Paper"]

'''Simplification Table:
Rock:
    Beats-Scissors
    Losses to - Papers
Paper:
    Beats-Rock
    Losses to- Scissors
Scissors:
    Beats-Paper
    Losses to- Rock'''

# Function for main game and user input is parameter
def game(usrply):
    # Options and Points are declared global for easier use
    global options,points
    #Random Play is selected from options list using choice function from random module
    randomplay= random.choice(options)
    # Only first character from the random choice is selected
    comp_play=randomplay[0].lower()
    # Only first character from the user input is selected
    inp=usrply[0].lower()
    
    if inp==comp_play:
        print(f"Computer's Play: {randomplay}\nTie!!!!!\nPoints: {points}")
    elif inp=="r" and comp_play=="s":
        points+=1
        print(f"Computer's Play: {randomplay}\nYou Win!!!\nPoints: {points}")
    elif inp=="r" and comp_play=="p":
        print(f"Computer's Play: {randomplay}\nYou Lose!!!\nPoints: {points}")
    elif inp=="s" and comp_play=="p":
        points+=1
        print(f"Computer's Play: {randomplay}\nYou Win!!!\nPoints: {points}")
    elif inp=="s" and comp_play=="r":
        print(f"Computer's Play: {randomplay}\nYou Lose!!!\nPoints: {points}")
    elif inp=="p" and comp_play=="r":
        points+=1
        print(f"Computer's Play: {randomplay}\nYou Win!!!\nPoints: {points}")
    elif inp=="p" and comp_play=="s":
        print(f"Computer's Play: {randomplay}\nYou Lose!!!\nPoints: {points}")

if __name__=="__main__":
    text="WELCOME TO QUIZ GAME"
    width=70
    head_txt=text.center(width)
    print(head_txt+"\n")
    print("Press E to exit")
    for i in range(4):
        print(i)
        sleep(1)
    while True:
        usrply=input("Input: ")
        game(usrply)
        if usrply=="E" or usrply=="e":
            break
    print("\nThank You For Playing")


