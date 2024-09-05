Balance        = 0
Income         = []
Income_source  = []
Expense        = []
Expense_source = []

while True:
    print("Total Balance ", Balance)
    print("Type 1 for add income ")
    print("Type 2 for add expense ")
    print("Type 3 for check income ")
    print("Type 4 for check expense ")
    print("Type 5 for exit ")

    choice = int(input("Enter "))    


    if choice == 1:
        income, Income_source = input("Enter Income and source seperate by space ").split()
        income                = int(income)
        Income_source         = str(Income_source)
        Balance              += income
        print(Balance)

    elif choice == 2:
        Expense, Expense_source = input("Enter Income and source seperate by space ").split()
        Expense                 = int(Expense)
        Expense_source          = str(Expense_source)
        Balance                -= Expense
        print(Balance)

    elif choice == 3:
        print(Income," ", Income_source)

    elif choice == 4:
        print(Expense," ", Expense_source)

    else:
        break


