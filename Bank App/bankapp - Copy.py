import tkinter as tk
from tkinter import *
from tkinter import font

def save_info():
    account_number_info = account_number.get()
    account_name_info = account_name.get()
    password_info = password.get()
    print(account_number_info, account_name_info, password_info)

    file = open("bankdata.txt", "a")
    file.write("\n")
    file.write(account_number_info + ",")
    file.write(account_name_info + ",")
    file.write(password_info)
    file.close()
    print("User ", account_name_info, "has been registered successfully")

def check(account_number_check,password1_check):
    success = False
    account_number_check = account_number_entry1.get()
    password1_check = password_entry1.get()
    file = open("bankdata.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a==account_number_check and b==password1_check):
            success=True
            print(success)
        else:
            print("failed")

win = tk.Tk()

style1 =font.Font(size=25)

Welcome = Frame(win)
Home = Frame(win)
CreateAccount = Frame(win)
ExistingAccount = Frame(win)

Welcome.grid(row=0, column=0, sticky="nsew")
Home.grid(row=0, column=0, sticky="nsew")
CreateAccount.grid(row=0, column=0, sticky="nsew")
ExistingAccount.grid(row=0, column=0, sticky="nsew")

#WELCOME PAGE 
lbl1 = Label(Welcome, text="LOGO", font=('Arial', 18))
lbl1.pack(padx=280, pady=20)

btnContinue = Button(Welcome, text="Show page 2", command=lambda: Home.tkraise(), font=style1)
btnContinue.pack()

#HOME PAGE
lblHomeHeading = Label(Home, text="HOME", font=('Arial', 18))
lblHomeHeading.pack(padx=280, pady=20)

btnCreateAccount = Button(Home, text="Create Account", command=lambda: CreateAccount.tkraise(), font=style1)
btnCreateAccount.pack(pady=20)

btnExistingAccount = Button(Home, text="Existing Account", command=lambda: ExistingAccount.tkraise(), font=style1)
btnExistingAccount.pack(pady=20)


#CREATE ACCOUNT
account_number = StringVar()
account_name = StringVar()
password = StringVar()

heading = Label(CreateAccount, text="Create Account", bg="grey", fg="black", width="95", height="5")
heading.pack()


account_number_text = Label(CreateAccount, text="Enter Account Number: ")
account_number_text.pack(pady=20)

account_number_entry = Entry(CreateAccount, textvariable= account_number, width="30")
account_number_entry.pack(pady=20)

account_name_text = Label(CreateAccount, text="Enter Account Holder Name: ")
account_name_text.pack(pady=20)

account_name_entry = Entry(CreateAccount, textvariable= account_name, width="30")
account_name_entry.pack(pady=20)

password_text = Label(CreateAccount, text="Enter Account Password: ")
password_text.pack(pady=20)

password_entry = Entry(CreateAccount, textvariable= password, width="30")
password_entry.pack(pady=20)

btnConfirm = Button(CreateAccount, text="Confirm", command=save_info, font=style1)
btnConfirm.pack(pady=20)
btnHome = Button(CreateAccount, text="Home", command=lambda: Home.tkraise(), font=style1)
btnHome.pack(pady=20)

#EXISTING ACCOUNT
account_number1 = StringVar()
password1 = StringVar()

heading = Label(ExistingAccount, text="Existing Account", bg="grey", fg="black", width="95", height="5")
heading.pack()

account_number_text1 = Label(ExistingAccount, text="Enter Account Number: ")
account_number_text1.pack(pady=20)

account_number_entry1 = Entry(ExistingAccount, textvariable= account_number1, width="30")
account_number_entry1.pack(pady=20)

account_number_text1 = Label(ExistingAccount, text="Enter Account Number: ")
account_number_text1.pack(pady=20)

password_entry1 = Entry(ExistingAccount, textvariable= password1, width="30")
password_entry1.pack(pady=20)

btnConfirmE = Button(ExistingAccount, text="Confirm", command=check, font=style1)
btnConfirmE.pack(pady=20)
btnHome = Button(ExistingAccount, text="Home", command=lambda: Home.tkraise(), font=style1)
btnHome.pack(pady=20)

Welcome.tkraise()
win.geometry("650x650")
win.resizable(False, False)
win.mainloop()