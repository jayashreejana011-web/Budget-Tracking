import json
from datetime import date

file = "transactions.json"


def load():
    try:
        f = open(file, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []


def save(data):
    f = open(file, "w")
    json.dump(data, f, indent=4)
    f.close()


def add(data):
    print("\nAdd Transaction")

    while True:
        typ = input("Type (income/expense): ").lower()

        if typ == "income" or typ == "expense":
            break

        print("Enter income or expense.")

    while True:
        try:
            amt = float(input("Amount: "))

            if amt > 0:
                break

            print("Amount must be greater than 0.")

        except:
            print("Enter a valid amount.")

    cat = input("Category: ")

    while cat == "":
        print("Category cannot be empty.")
        cat = input("Category: ")

    dt = input("Date (YYYY-MM-DD) [today]: ")

    if dt == "":
        dt = str(date.today())

    note = input("Note: ")

    data.append({
        "type": typ,
        "amount": amt,
        "category": cat,
        "date": dt,
        "note": note
    })

    save(data)
    print("Transaction added.")


def summary(data):
    income = 0
    expense = 0

    for x in data:
        if x["type"] == "income":
            income += x["amount"]
        else:
            expense += x["amount"]

    print("\n--- Summary ---")
    print("Total Income: ₹", format(income, ".2f"))
    print("Total Expenses: ₹", format(expense, ".2f"))
    print("Balance: ₹", format(income - expense, ".2f"))


def category(data):
    if len(data) == 0:
        print("No transactions found.")
        return

    cat = {}

    for x in data:
        name = x["category"]

        if name not in cat:
            cat[name] = [0, 0]

        if x["type"] == "income":
            cat[name][0] += x["amount"]
        else:
            cat[name][1] += x["amount"]

    print("\n--- Category Summary ---")

    for name in cat:
        print("\nCategory:", name)
        print("Income: ₹", cat[name][0])
        print("Expense: ₹", cat[name][1])


def show(data):
    if len(data) == 0:
        print("No transactions found.")
        return

    print("\n--- Transactions ---")

    for i in range(len(data)):
        x = data[i]

        print(
            i + 1,
            x["type"],
            "₹" + str(x["amount"]),
            x["category"],
            x["date"],
            x["note"]
        )

def edit(data):
    show(data)

    if len(data) == 0:
        return

    try:
        n = int(input("Enter number to edit: "))

        if n < 1 or n > len(data):
            print("Invalid number.")
            return

        x = data[n - 1]

        typ = input("Type: ")

        if typ == "income" or typ == "expense":
            x["type"] = typ

        amt = input("Amount: ")

        if amt != "":
            try:
                amt = float(amt)

                if amt > 0:
                    x["amount"] = amt

            except:
                print("Invalid amount.")

        cat = input("Category: ")

        if cat != "":
            x["category"] = cat

        dt = input("Date: ")

        if dt != "":
            x["date"] = dt

        x["note"] = input("Note: ")

        save(data)
        print("Transaction updated.")

    except:
        print("Invalid input.")

def delete(data):
    show(data)

    if len(data) == 0:
        return

    try:
        n = int(input("Enter number to delete: "))

        if n >= 1 and n <= len(data):
            data.pop(n - 1)
            save(data)
            print("Transaction deleted.")
        else:
            print("Invalid number.")

    except:
        print("Invalid input.")

def main():
    data = load()

    print("\nWelcome to Budget Tracker!")

    while True:
        print("\n1. Add transaction")
        print("2. View summary")
        print("3. View by category")
        print("4. Edit transaction")
        print("5. Delete transaction")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add(data)

        elif choice == "2":
            summary(data)

        elif choice == "3":
            category(data)

        elif choice == "4":
            edit(data)

        elif choice == "5":
            delete(data)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()