Balance = 0
Income  = []
Expense = []
while True:
    print("Total Balance ", Balance)
    print("Type 1 for add income ")
    print("Type 2 for add expense ")
    print("Type 3 for exit ")

    choice = int(input("Enter "))    


    if choice == 1:
        income, source = input("Enter Income and what for ").split()
        income       = int(income)
        source       = str(source)
        Balance      = Balance + income
        print(Balance)
    elif choice == 2:
        Expense, Transaction = input("Enter Income and what for ").split()
        Expense      = int(Expense)
        Transaction  = str(Transaction)
        Balance      = Balance - Expense
        print(Balance)
    else:
        break


