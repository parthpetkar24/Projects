#-------------------------------Simple 5 Questions Quiz Game-------------------------------------------------

import random                                   # random module imported to select questions randomly
from time import sleep                          # time module to delay incoming question using sleep function                                                 

point=0                                         # Total Score of player
Lost=False                                      # Variable to tell if player lost the game or not

# Dictionary of Questions with their options and answers
stack={
        "questions":["Which code reverses a string in Python?","What is the output of this code?\nprint(2 + 3 * 4)","Which code checks if a number is even?","What is the result of this code? \na = [1, 2, 3]\nprint(a[-1])","Which code finds the largest of three numbers a, b, c?"],
        "A":["str[::-1]","20","if num % 2 == 0:","1","max(a, b, c)"],
        "B":["reverse(str)","14","if num / 2 == 0:","2","largest(a, b, c)"],
        "C":["str.reverse()","24","if num % 2 == 1:","3","a > b > c"],
        "D":["str[1:]","10","if num // 2 == 0:","Error","a + b + c"],
        "Answer":["A","B","A","C","A"]
    }

# Function to play quiz game
def  quiz():
    global point,Lost,stack                                         # Variables are declared global so they can easily be accessed
    
    index=random.randint(0,len(stack["questions"])-1)               # Select Random question from the dictionary and store its index
    # Print question and their options accessed using their index
    print("\n"+stack["questions"][index])
    print(f"A) {stack['A'][index]}")
    print(f"B) {stack['B'][index]}")
    print(f"C) {stack['C'][index]}")
    print(f"D) {stack['D'][index]}")

    # Take User answer using input function
    lock=input("\nYour Answer A / B / C / D ?: ")

    #Check if the user answer matches the actual answer
    if lock.upper()==stack["Answer"][index]:
        sleep(1)
        print("Correct!!!!!!!!")
        point=point + 1
        print("Current Points: ",point)
        pass
    else:
        print("Sorry You Lose!!!")
        print("Final Points: ",point)
        Lost=True

    for key in stack:
        stack[key].pop(index)

# Function to ask user if they want to continue the game
def cont():
    cont=input("\nContinue?? (Y/N):")
    return cont.lower()


# Main Execution
text="WELCOME TO QUIZ GAME"
width=70
head_txt=text.center(width)
print(head_txt+"\n")
start=input("Start the Game? (Y/N): ")
if(start[0].lower()=="y"):
    print("Here we go")
    sleep(1)
    quiz()
    while Lost==False and cont()=="y" :
        sleep(1)
        quiz()
        if Lost:
            print(f"\nFinal Score: {point}")
            exit()
        elif len(stack["questions"]) == 0:
            print("\nAll questions attempted!")
            print(f"\nFinal Score: {point}")
            exit()
        else:
            print(f"\nFinal Score: {point}")
    

else:
    print("Thank You For Running this Script")
    print(f"\nFinal Score: {point}")
    exit()

