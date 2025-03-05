
import os
from datetime import datetime

# File to store transaction records
FILE_NAME = "expenses.txt"

# Function to add a transaction (income/expense)
def add_transaction():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Income, Food, Transport, Shopping, etc.): ")
    description = input("Enter description: ")
    transaction_type = input("Type (Income/Expense): ").strip().lower()

    if transaction_type not in ["income", "expense"]:
        print("Invalid!! Please enter either 'Income' or 'Expense'")
        return
    
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category},{description},{transaction_type},{date}\n")
    
    print("Transaction added successfully!")




# Function to view all transactions
def view_transactions():
    if not os.path.exists(FILE_NAME):
        print("No transactions found!")
        return
    
    with open(FILE_NAME, "r") as file:
        transactions = file.readlines()
    
    if not transactions:
        print("No transactions recorded yet")
        return

    print("\nAmount|Category|Description|Type|Date")
    print("-" * 50)
    for trans in transactions:
        print(" | ".join(trans.strip().split(",")))



# Function to search for transactions by category
def search_transaction():
    keyword = input("Enter category or keyword to search: ").strip().lower()
    found = False

    with open(FILE_NAME, "r") as file:
        transactions = file.readlines()
    
    print("\nMatching Transactions:")
    print("Amount | Category | Description | Type|Date")
    print("-" * 50)
    
    for trans in transactions:
        if keyword in trans.lower():
            print(" | ".join(trans.strip().split(",")))
            found = True
    
    if not found:
        print("No matching transactions found.")


# Function to show financial summary
def financial_summary():
    if not os.path.exists(FILE_NAME):
        print("No transactions found!")
        return
    
    total_income = 0
    total_expense = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")  
            print(data)
            amount = float(data[0])  
            transaction_type = data[3].strip().lower()  

            if transaction_type == "income":
                total_income += amount 
            elif transaction_type == "expense":
                total_expense += amount 

    net_balance = total_income - total_expense  

    # Display summary
    print("\nFinancial Summary")
    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expense:.2f}")
    print(f"Net Balance:  ₹{net_balance:.2f}")
    
    
# Menu
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Search Transaction")
    print("4. Financial Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        search_transaction()
    elif choice == "4":
        financial_summary()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
