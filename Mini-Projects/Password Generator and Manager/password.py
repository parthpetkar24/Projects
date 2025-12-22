import pandas as pd
import random
import string
import os


def generate_password():
    characters=list(string.ascii_letters)
    numbers=list(string.digits)
    characters_numbers=characters+numbers
    password=""
    while len(password)<=16:
        passchar=random.choice(characters_numbers)
        password+=passchar
    return password

def store_password(purpose,password):
    manager={"Purpose":purpose,"Password":password}
    passmanager=pd.DataFrame([manager])
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.csv")

    if os.path.exists(file_path):
        passmanager.to_csv(file_path, mode="a", header=False, index=False)
    else:
        passmanager.to_csv(file_path, index=False)
    return file_path

def view_passwords():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    view=pd.read_csv('data.csv')
    print(view)

def search(app):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    manage=pd.read_csv('data.csv')
    mask=manage["Purpose"].str.lower()==app.lower()
    if mask.any():
        row=manage.loc[mask]
        print(row)
    else:
        print("Not Found!")

if __name__ == "__main__":
    text="Welcome To Password Manager"
    width=100
    print(text.center(width))

    while True:
        print("\nOperations Available: 1.Generate New Password\t2.Store Password\t3.View All Passwords\t4.Search for Passoword\t5.Exit")
        op=int(input("Enter Operation(1/2/3/4/5): "))
        match(op):
            case 1: 
                newpass=generate_password()
                print(f"New Generated Password: {newpass}")
                generated=True
            case 2:
                if generated:
                    purpose=input("Enter the Application or Website for the password: ")
                    store_password(purpose,newpass)
                    print("Stored Successfully!")
                    newpass=""
                    generated=False
                else:
                    print("Generate a Password first!!")
            case 3: view_passwords()
            case 4: 
                app=input("Enter Application or Website: ")
                search(app)
            case 5: break
            case _:
                print("Invalid Operation!")


