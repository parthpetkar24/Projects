import random

life=5
score=0
best_attempt=0

def easylevel():
    comp_guess=random.randrange(1,51)
    user_guess=int(input("Enter Your Best Guess from 1 to 50: "))
    if user_guess>50 or user_guess<1:
        print("Number Out of Range!!!")
    else:
        if user_guess==comp_guess:
            print(f"Awesome!!! Got it Right!! The number was {comp_guess}")
            score+=1
        elif user_guess<comp_guess:
            print("Try Higher!")
            life-=1
        elif user_guess>comp_guess:
            print("Try Lower!")
            life-=1

if __name__=="__main__":
    text="Welcome To Number Guessing Game"
    width=100
    print(text.center(width))
    while(life!=0):
        try:
            level=input("Select Level (Easy/Medium/Hard): ")
            if level.lower()=="easy":
                easylevel()

        except Exception as e:
            print("\nEnter Appropriate Level")