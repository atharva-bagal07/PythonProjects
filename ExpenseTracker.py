import os
import csv
from pyttsx3 import *

food_expenses = 0
Sports_expenses = 0
Travel_expenses = 0
total_expenses = 0

date = ''
engine = init()

if not os.path.exists("expenses.csv"):
    with open("expenses.csv", 'w') as f:
        writeobj = csv.writer(f)
        write_row = writeobj.writerow(["Date", 'Category', 'Amount_Spent','Total_Expenses'])

def calculate_expense():
    global food_expenses, Sports_expenses, Travel_expenses, date, total_expenses
    # engine.say("Enter the date")
    engine.runAndWait()
    date = input("Enter the date (DD/MM/YY): ")
#     engine.say("Enter the amount you spent")
    engine.runAndWait()
    amount_spent = int(input("Enter the amount you spent: "))
    print("Under which category would u like to categorise your spending?\n 1. Food\n 2. Sports\n 3. Travel")
#     engine.say("Enter your Category")
    engine.runAndWait()
    category_choice = input("Enter your Category: ")

    if category_choice.lower().strip() == "food":
        food_expenses += amount_spent
#         engine.say("Expense added")
        engine.runAndWait()
        print("Expense added.")

    elif category_choice.lower().strip() == "sports":
        Sports_expenses += amount_spent
#         engine.say("Expense added")
        engine.runAndWait()
        print("Expense added.")

    elif category_choice.lower().strip() == 'travel':
        Travel_expenses += amount_spent
#         engine.say("Expense added")
        engine.runAndWait()
        print("Expense added.")

    elif print(f"Expense added under new Category {category_choice}"):
        # engine.say(f"Expense added under new Category {category_choice}")
        engine.runAndWait()


    else:
        print("Invalid input! Please enter a valid Category..")
#

    total_expenses = load_expense() + amount_spent
    if not os.path.exists("Total_expenses.txt"):
        with open("Total_expenses.txt", 'w') as f1:
            f1.write(f"{total_expenses}\n")
    else:
        with open("Total_expenses.txt",'a') as f3:
            f3.write(f"{total_expenses}\n")

    with open("expenses.csv",'a') as f:
        writeobj = csv.writer(f)
        writeobj.writerow([date,category_choice,amount_spent,load_expense()])

def load_expense():
    if os.path.exists("Total_expenses.txt"):
        with (open("Total_expenses.txt") as f4):
            y = 0
            x = f4.readlines()
            # first = int(x[0])
            y = y + int(x[len(x)-1])
            return y
    else:
        return 0

def load_expense_for_view():

    if os.path.exists("Total_expenses.txt"):
        with (open("Total_expenses.txt") as f4):
            y = 0
            x = f4.readlines()
            # first = int(x[0])
            y = y + int(x[len(x)-1])
            return y
    else:
        print("You have not made any expenses yet!")


def view_monthly_expenses():
    pass

def view_expense():
    global date
    if date != '':
        
#         engine.say(f"Your total Expenses till date {date} are Rs.{total_expenses}")
        engine.runAndWait()
        print(f'''\n\t\tFood expenses till {date}: Rs.{food_expenses}
        Sports expenses till {date}: Rs.{Sports_expenses}
        Travel expenses till {date}: Rs.{Travel_expenses}
        Your total Expenses till {date} are Rs.{total_expenses}''')
    else:
        with open("expenses.csv") as f:
            print(f"Your expenses till the day are: {load_expense_for_view()}")

while True:
#     engine.say("Which function would you like to perform? 1 Add Expenses\n 2 View Expenses\n 3 Exit")
    engine.runAndWait()
    
    print(" 1.Add Expenses\n 2.View Expenses\n 3.Exit")
#     engine.say("Enter your choice between 1 and 3")
    engine.runAndWait()
    choice = int(input("Enter your choice(1-3): "))
    if choice == 1:
        calculate_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        if os.path.exists("expenses.csv"):
            os.startfile("C:\\Python projects\\expenses.csv")
        break
    else:
        print("Invalid Choice! Enter your choice between 1 and 3")
        continue
#     engine.say("Do you want to continue?")
    engine.runAndWait()

    ch =input("Do you want to continue?(y/n): ")
    if 'n' in ch.lower():
        if os.path.exists("expenses.csv"):
            os.startfile("C:\\Python projects\\expenses.csv")
        break
    elif ch.lower()!='y' and 'n':
        print("Invalid input! Please pass a valid choice!")
