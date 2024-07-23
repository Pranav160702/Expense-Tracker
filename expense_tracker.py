from expenses import Expense
from datetime import datetime, timedelta

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = 'expenses.csv'
    budget = 2000

    # Get user input for expense.
    expense = get_user_expense()
    
    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and Summarize expenses.
    summarize_expenses(expense_file_path, budget)


# START GET USER EXPENSE FUNCTION 
def get_user_expense():
    print(f"🎯 Getting User Expense...")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
     
    expense_category = [
        "🍔 Food", 
        "🏠 Home", 
        "💼 Work", 
        "🚇 Transportation", 
        "🛒 Shopping",
        "🎉 Entertainment", 
        "💸 Others"
    ]

    while True:
        print(f"🎯 Select Expense Category:")
        for index, category in enumerate(expense_category):
            print(f"{index + 1}. {category}")
        
        try:
            value_range = f"[1 - {len(expense_category)}]"
            selected_index = int(input(f"Enter a Category Number{value_range}:")) - 1
        except ValueError:
            print(f"🚫 Invalid Category! Please try again...")

    
        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            
            new_expense = Expense(
                name = expense_name, 
                category = selected_category, 
                amount = expense_amount
                )
            return new_expense
        
        else:
            print(f"🚫 Invalid Category! Please try again...")
# END GET USER EXPENSE FUNCTION

# START SAVE EXPENSE FUNCTION
def save_expense_to_file(expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")

    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.category}, {expense.name},  {expense.amount}\n")
# END SAVE EXPENSE FUNCTION


# START SUMMARIZE EXPENSES FUNCTION
def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense...")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_category, expense_name, expense_amount= line.strip().split(",")
            line_expense = Expense(
                name = expense_name, 
                category = expense_category, 
                amount = float(expense_amount) 
                )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    # Expenses by category
    print("Expenses By Category📈: ")
    for category, amount in amount_by_category.items():
        print(f"{category}: ${amount:.2f}")

    # Total Spend 
    total_spend = sum([x.amount for x in expenses])
    print(f"💸You've spent: ${total_spend:.2f} ")

    # Remaining Budget
    remaining_budget = budget - total_spend
    print(f"✅Budget Remaining ${remaining_budget:.2f} ")

    # Remaining Days in Month
    today = datetime.today()
    next_month = (today.replace(day=28) + timedelta(days=4)).replace(day=1)
    remaining_days = (next_month - today).days

    # Budget Per day
    daily_budget = remaining_budget / remaining_days
    print(f"👉 Budget Per Day : ${daily_budget:.2f}")

# END SUMMARIZE EXPENSES FUNCTION


if __name__ == "__main__":
    main()