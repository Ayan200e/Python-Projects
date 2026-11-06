import csv
import os

FILENAME = "expenses.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category (e.g., Food, Travel, Utilities): ").strip().capitalize()
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    description = input("Enter brief description: ").strip()
    
    initialize_csv()
    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
        
    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Recorded Expenses ---")
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return
        
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("No expenses found in the record.")
            return
            
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
        print("-" * 60)
        for row in rows[1:]:
            print(f"{row[0]:<12} | {row[1]:<15} | {row[2]:<10} | {row[3]}")

def filter_and_summarize():
    print("\n--- Expense Statistics & Filtering ---")
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return
        
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
        
    if not expenses:
        print("No data available.")
        return
        
    total_spend = sum(float(row['Amount']) for row in expenses)
    print(f"\nTotal Overall Spending: {total_spend:.2f}")
    
    category_totals = {}
    for row in expenses:
        cat = row['Category']
        amt = float(row['Amount'])
        category_totals[cat] = category_totals.get(cat, 0.0) + amt
        
    print("\nSpending by Category:")
    for cat, amt in category_totals.items():
        print(f"  - {cat}: {amt:.2f}")
        
    filter_choice = input("\nWould you like to filter by category? (y/n): ").strip().lower()
    if filter_choice == 'y':
        target_cat = input("Enter category to filter: ").strip().capitalize()
        filtered = [row for row in expenses if row['Category'] == target_cat]
        if filtered:
            print(f"\nExpenses for Category: {target_cat}")
            print(f"{'Date':<12} | {'Amount':<10} | {'Description'}")
            print("-" * 45)
            for row in filtered:
                print(f"{row[0]:<12} | {row[2]:<10} | {row[3]}")
        else:
            print(f"No expenses found under category '{target_cat}'.")

def main():
    initialize_csv()
    while True:
        print("\n--- Project 03: Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary & Filter")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_and_summarize()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
