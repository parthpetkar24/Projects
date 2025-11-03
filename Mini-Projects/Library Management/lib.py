import os
import pandas as pd
from time import sleep

def add_book(libFrame):
    book_id=int(input("\nEnter Book Id: "))
    book_name=input("Enter Book Name: ")
    book_author=input("Enter Book Author Name: ")
    book_year=input("Enter Book Publication Year: ")
    libFrame.loc[len(libFrame)]={
        "Id":book_id,
        "Books":book_name.lower(),
        "Author":book_author.lower(),
        "Year":book_year}
    libFrame.to_csv('Library Management/index.csv',index=False)
    print("\nBook Added Successfully!!")

def issue_book(libFrame,issueFrame):
    issue_id=int(input("Enter Book Id to Issue: "))
    for id in libFrame["Id"]:
        if issue_id in libFrame["Id"].values:
            issue_to=input("Enter Borrower Name: ")
            issue_contact=int(input("Enter Borrower Contact: "))
            issue_date=input("Enter Issue Date: ")
            issueFrame.loc[len(issueFrame)]={
                "Id":issue_id,
                "Books":libFrame.loc[libFrame["Id"] == issue_id, "Books"].values[0],
                "Borrower_Name":issue_to,
                "Contact":issue_contact,
                "Issue_Date":issue_date
                }
            indice=libFrame[libFrame["Id"]==issue_id].index
            libFrame.drop(indice,inplace=True)
            libFrame.to_csv('Library Management/index.csv')
            issueFrame.to_csv('Library Management/issue.csv')
        else:
            print("Book Not Avaliable in Library!")
            break 

def remove_book(libFrame):
    found=False
    removeby=int(input("\nRemove Book by: \n1.Id \t2.Name\nInput: "))
    if removeby==1:
        removebyid=int(input("Enter Book Id: "))
        for id in libFrame["Id"]:
            if id == removebyid:
                indice=libFrame[libFrame["Id"]==removebyid].index
                libFrame.drop(indice,inplace=True)
                libFrame.to_csv('Library Management/index.csv',index=False)
                print("Book Removed Successfully!")
                found=True
        if not found:
            print("Book Not Found!")
    elif removeby==2:
        removebyname=input("Enter Name of Book: ")
        for name in libFrame["Books"]:
            if name == removebyname.lower():
                indice=libFrame[libFrame["Books"]==removebyname].index
                libFrame.drop(indice,inplace=True)
                libFrame.to_csv('Library Management/index.csv',index=False)
                print("Book Removed Successfully!")
                found=True
        if not found:
            print("Book Not Found!")
    else:
        print("Invalid Input!")

def view_current(libFrame):
    print("Current Library Data: \n")
    print(libFrame)

if __name__=="__main__":
    print("Welcome to Library Managment System!\n")
    sleep(1)
    file_name='Library Management/index.csv'
    issuer_file='Library Management/issue.csv'
    if os.path.isfile(file_name) and os.path.isfile(issuer_file):
        print("Opening File...")
    else:
        lib={
            "Id":[],
            "Books":[],
            "Author":[],
            "Year":[]
        }
        issue={
            "Id:":[],
            "Books":[],
            "Borrower_Name":[],
            "Contact":[],
            "Issue_Date":[]
        }
        libFrame=pd.DataFrame(lib)
        issueFrame=pd.DataFrame(issue)
        libFrame.to_csv('Library Management/index.csv',index=False)
        issueFrame.to_csv('Library Management/issue.csv',index=False)
        print("File Created!")

    libFrame=pd.read_csv('Library Management/index.csv')
    issueFrame=pd.read_csv('Library Management/issue.csv')
    print("\nLibrary Manager Opened!")
    while True:
        print("\nOperations Available:\n1.Add Book\t2.Issue Book\t3.Remove book from Library\n4.View Current Books in Library\t5.Exit")
        action=int(input("Enter Index of Operation to be performed(1/2/3/4): "))
        match(action):
            case 1:
                add_book(libFrame)
            case 2:
                issue_book(libFrame,issueFrame)
            case 3:
                remove_book(libFrame)
            case 4:
                view_current(libFrame)
            case 5:
                print("Thank You for using Library Management System! ")
                break
            case _:
                print("Invalid Operation")
                

