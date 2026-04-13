import random

levels={
    "easy":[1,20,5],
    "medium":[1,50,7],
    "hard":[1,100,10]
}
score=0
best_attempt=0

def play(level):
    global score
    life,life_before=levels[level][2]
    comp_guess=random.randrange(levels[level][0],levels[level][1]+1)
    while(life!=0):
        user_guess=int(input(f"\nEnter Your Best Guess from {levels[level][0]} to {levels[level][1]}: "))
        if user_guess<levels[level][0] or user_guess>levels[level][1]:
            print("Number Out of Range!!!")
            break
        else:
            if user_guess==comp_guess:
                print(f"Awesome!!! Got it Right!! The number was {comp_guess}")
                score+=1
                best_attempt=life_before-life
                break

            elif user_guess<comp_guess:
                life-=1
                print(f"Try Higher!\nLife Left: {life}")
                
            elif user_guess>comp_guess:
                life-=1
                print(f"Try Lower!\nLife Left: {life}")
        
        if life == 0:
            print(f"\nBad Luck!!! Out of Lives!")
            print(f"The number was {comp_guess}")
            print(f"Score: {score}")
            print(f"Best Attempt: {best_attempt}")
    return score,best_attempt

if __name__=="__main__":
    text="Welcome To Number Guessing Game"
    width=100
    print(text.center(width))
  
    while(True):    
        print("\nEnter 'q' to exit")
        level=input("Select Level (Easy/Medium/Hard): ")
        if level.lower() in levels:
            play(level.lower())
        elif level.lower()=="q":
            print(f"Thank You for Playing!!\nScore: {score}")
            print(f"Best Attempt: {best_attempt}")
            break
        else:
            print("\nEnter Appropriate Level")