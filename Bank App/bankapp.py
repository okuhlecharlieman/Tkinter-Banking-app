import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import main

def save_info():
    account_number_info = account_number.get()
    account_name_info = account_name.get()
    password_info = password.get()
    print(account_number_info, account_name_info, password_info)

    file = open("bankdata.txt", "a")
    file.write("\n")
    file.write("AccountNumber = " + account_number_info)
    file.write("\n")
    file.write("Password = " + password_info)
    file.close()
    print("User ", account_name_info, "has been registered successfully")

    file = open("transactiondata.txt", "a")
    file.write("\n")
    file.write("AccountNumber = " + account_number_info)
    file.write("\n")
    file.write("Balance = 0")
    file.close()
    print("User ", account_name_info, "transaction data has been registered successfully")
    account_number_entry_create.delete(0, 'end')
    account_name_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    

def confirm_and_raise():
    check()

def check():
    entered_account_number = account_number1.get()
    entered_password = password1.get()
    delimeter = '='
    file = open("bankdata.txt", "r")
    found = False
    for line in file:
        line = line.rstrip('\n')
        if line.startswith('AccountNumber'):
            AccountNumber = line[line.index(delimeter)+1:].replace(" ","")
        elif line.startswith('Password'):
            Password = line[line.index(delimeter)+1:].replace(" ","")
        if entered_account_number == AccountNumber and entered_password == Password:
            found = True
            break
    file.close()

    if found:
        success_message = "Welcome! to CitiBank"
        messagebox.showinfo("Login Successful!", success_message)
        MainMenu.tkraise()
    else:
        error_message = "Invalid account number or password!"
        messagebox.showerror("Login Failed!", error_message)
    account_number_entry1.delete(0, 'end')
    password_entry1.delete(0, 'end')
    

def Depo():
    deposit_amount = amount_deposit.get()
    entered_account_number = account_number_deposit.get()
    
    delimeter = '='
    file = open("transactiondata.txt", "r")
    updated_lines = []
    found = False
    for line in file:
        line = line.rstrip('\n')
        if line.startswith('AccountNumber'):
            AccountNumber = line[line.index(delimeter)+1:].replace(" ","")
            updated_lines.append(line)
        elif line.startswith('Balance'):
            Balance = line[line.index(delimeter)+1:].replace(" ","")
            if entered_account_number == AccountNumber:
                found = True
                account_balance_value = int(Balance)
                new_balance_value = account_balance_value + int(deposit_amount)
                display_value = str(new_balance_value)
                updated_lines.append("Balance = " + display_value)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    file.close()
    
    if found:
        with open("transactiondata.txt", "w") as file:
            for index, line in enumerate(updated_lines):
                if index == len(updated_lines) - 1:
                    file.write(line)
                else:
                    file.write(line + "\n")
        success_message = "New balance: " + str(new_balance_value)
        messagebox.showinfo("Deposit Successful!", success_message)
    else:
        error_message = "Invalid account number!"
        messagebox.showerror("Deposit Failed!", error_message)
    account_deposit_entry.delete(0, 'end')
    account_number_entry_deposit.delete(0, 'end')

def With():
    withdraw_amount = amount.get()
    entered_account_number = account_number_withdraw.get()
    
    delimeter = '='
    file = open("transactiondata.txt", "r")
    updated_lines = []
    found = False
    for line in file:
        line = line.rstrip('\n')
        if line.startswith('AccountNumber'):
            AccountNumber = line[line.index(delimeter)+1:].replace(" ","")
            updated_lines.append(line)
        elif line.startswith('Balance'):
            Balance = line[line.index(delimeter)+1:].replace(" ","")
            if entered_account_number == AccountNumber:
                found = True
                account_balance_value = int(Balance)
                new_balance_value = account_balance_value - int(withdraw_amount)
                updated_lines.append("Balance = " + str(new_balance_value))
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    file.close()
    
    if found:
        with open("transactiondata.txt", "w") as file:
            for index, line in enumerate(updated_lines):
                if index == len(updated_lines) - 1:
                    file.write(line)
                else:
                    file.write(line + "\n")
        success_message = "New balance: " + str(new_balance_value)
        messagebox.showinfo("Deposit Successful!", success_message)
    else:
        error_message = "Invalid account number!"
        messagebox.showerror("Deposit Failed!", error_message)
    account_withdrawl_entry.delete(0, 'end')
    account_number_entry_withdrawl.delete(0, 'end')


    
win = tk.Tk()

style1 =font.Font(size=25)

Home = Frame(win)
CreateAccount = Frame(win)
ExistingAccount = Frame(win)
MainMenu = Frame(win)
Transaction = Frame(win)
Depos = Frame(win)
Withdraw = Frame(win)

Home.grid(row=0, column=0, sticky="nsew")
CreateAccount.grid(row=0, column=0, sticky="nsew")
ExistingAccount.grid(row=0, column=0, sticky="nsew")
MainMenu.grid(row=0, column=0, sticky="nsew")
Transaction.grid(row=0, column=0, sticky="nsew")
Depos.grid(row=0, column=0, sticky="nsew")
Withdraw.grid(row=0, column=0, sticky="nsew")


#HOME PAGE
heading = Label(Home, text="HOME", bg="grey", fg="black", width="95", height="5")
heading.pack()

btnCreateAccount = Button(Home, text="Create Account", command=lambda: CreateAccount.tkraise(), font=style1)
btnCreateAccount.pack(pady=120)

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

account_number_entry_create = Entry(CreateAccount, textvariable= account_number, width="30")
account_number_entry_create.pack(pady=20)

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
account_number_text1.pack(pady=30)

account_number_entry1 = Entry(ExistingAccount, textvariable= account_number1, width="30")
account_number_entry1.pack(pady=30)

password_text1 = Label(ExistingAccount, text="Enter Password Number: ")
password_text1.pack(pady=30)

password_entry1 = Entry(ExistingAccount, textvariable= password1, width="30")
password_entry1.pack(pady=30)

btnConfirmE = Button(ExistingAccount, text="Confirm", command=confirm_and_raise, font=style1)
btnConfirmE.pack(pady=30)
btnHome = Button(ExistingAccount, text="Home", command=lambda: Home.tkraise(), font=style1)
btnHome.pack(pady=30)

#MAIN MENU
heading = Label(MainMenu, text="OPTIONS", bg="grey", fg="black", width="95", height="5")
heading.pack()

btnConfirm = Button(MainMenu, text="Transaction", command=lambda: Transaction.tkraise(), font=style1)
btnConfirm.pack(pady=200)

#TRANSACTION
heading = Label(Transaction, text="TRANSACTION", bg="grey", fg="black", width="95", height="5")
heading.pack()

btnConfirm = Button(Transaction, text="Deposit", command=lambda: Depos.tkraise(), font=style1)
btnConfirm.pack(pady=120)
btnHome = Button(Transaction, text="Withdrawal", command=lambda: Withdraw.tkraise(), font=style1)
btnHome.pack(pady=20)

#DEPOSIT
amount_deposit = StringVar()
account_number_deposit = StringVar()

heading = Label(Depos, text="DEPOSIT", bg="grey", fg="black", width="95", height="5")
heading.pack()

account_number_text = Label(Depos, text="Enter Deposit Amount: ")
account_number_text.pack(pady=30)

account_deposit_entry = Entry(Depos, textvariable= amount_deposit, width="30")
account_deposit_entry.pack(pady=30)

account_number_text = Label(Depos, text="Enter Account Number: ")
account_number_text.pack(pady=30)

account_number_entry_deposit = Entry(Depos, textvariable= account_number_deposit, width="30")
account_number_entry_deposit.pack(pady=30)

btnConfirm = Button(Depos, text="Deposit", command=Depo, font=style1)
btnConfirm.pack(pady=20)

btnTransaction = Button(Depos, text="Transaction", command=lambda: Transaction.tkraise(), font=style1)
btnTransaction.pack(pady=20)

#WITHDRAWL
amount = StringVar()
account_number_withdraw = StringVar()

heading = Label(Withdraw, text="WITHDRAWAL", bg="grey", fg="black", width="95", height="5")
heading.pack()


withdraw_text = Label(Withdraw, text="Enter the Amount: ")
withdraw_text.pack(padx=20, pady=30)

account_withdrawl_entry = Entry(Withdraw, textvariable= amount, width="30")
account_withdrawl_entry.pack(pady=30)

account_number_text = Label(Withdraw, text="Enter Account Number: ")
account_number_text.pack(padx=20, pady=30)

account_number_entry_withdrawl = Entry(Withdraw, textvariable= account_number_withdraw, width="30")
account_number_entry_withdrawl.pack(pady=30)

btnConfirm = Button(Withdraw, text="Withdraw", command=With, font=style1)
btnConfirm.pack(pady=20)

btnTransaction = Button(Withdraw, text="Transaction", command=lambda: Transaction.tkraise(), font=style1)
btnTransaction.pack(pady=20)

Home.tkraise()
win.geometry("650x650")
win.resizable(False, False)
main.root.mainloop()