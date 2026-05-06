import math
import json
import datetime
import os

storage=0

if __name__ =="__main__":
    title="Welcome To Simple Calculator"
    width=100
    print(title.center(width),"\n")
    for i in range(150):
        print("#",end="")
    first_entered=False
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data.json")
    print("\n")
    while(True):
        print("Operation Available: 1.Add\t2.Subtract\t3.Multiply\t4.Divide\t5.Advanced\t6.Clear\t7.History\t8.Exit")
        try:
            user_in=int(input("Enter Operation Number: "))
            if user_in not in range(1, 9):
                print("Enter Valid Operation Number")
        except ValueError as e:
            print("Enter Valid Number")

        if user_in==5 or user_in==6 or user_in==7 or user_in==8:
            pass
        else: 
            if first_entered==True:
                num1=storage
            else:
                num1=float(input("Enter Number: "))
                first_entered=True
            num2=float(input("Enter Number: "))
        
        match user_in:
            case 1:
                    add_fun=lambda num1,num2: num1+num2
                    storage=add_fun(num1,num2)
                    print(f"Result: {storage}\n")
            case 2:
                    sub_fun=lambda num1,num2: num1-num2
                    storage=sub_fun(num1,num2)
                    print(f"Result: {storage}\n")
            case 3:
                    multi_fun=lambda num1,num2: num1*num2
                    storage=multi_fun(num1,num2)
                    print(f"Result: {storage}\n")
            case 4:
                    try:
                        div_fun=lambda num1,num2: num1/num2
                        storage=div_fun(num1,num2)
                        print(f"Result: {storage}\n")
                    except ZeroDivisionError as e:
                         print("Cannot Divide by Zero")
            case 5:
                    print("Advance Operations: 1.Sine\t2.Cos\t3.Tan\t4.Cosine\t5.Sec\t6.Cot")
                    try:
                        advance_user_in=int(input("Enter Operation Number: "))
                        if advance_user_in not in range(1, 7):
                            print("Enter Valid Operation Number")
                    except Exception as e:
                        print("Enter Valid Operation Number(For e.g. If Sine enter 1)")
                    match advance_user_in:
                            case 1: 
                                storage=math.sin(storage)
                                print(f"Result: {storage}\n")
                            case 2: 
                                storage=math.cos(storage)
                                print(f"Result: {storage}\n")
                            case 3: 
                                storage=math.tan(storage)
                                print(f"Result: {storage}\n")
                            case 4: 
                                storage=1/(math.sin(storage))
                                print(f"Result: {storage}\n")
                            case 5: 
                                storage=1/(math.cos(storage))
                                print(f"Result: {storage}\n")
                            case 6: 
                                storage=1/(math.tan(storage))
                                print(f"Result: {storage}\n")
                            case _: 
                                continue
            case 6:
                    
                    entry={"datetime":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"last_result":storage}
                    try:
                        with open(file_path, "r") as file:
                            data = json.load(file)

                    except (FileNotFoundError, json.JSONDecodeError):
                        data = []
                    data.append(entry)
                    with open(file_path, "w") as file:
                        json.dump(data, file, indent=4)  
                    storage=0
                    first_entered=False

            case 7:
                    with open(file_path,"r") as file:
                        data=json.load(file)
                    print(data,"\n")
            case 8:
                    break
            case _:
                    pass
                

