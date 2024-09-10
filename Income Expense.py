Balance        = 0
Incomes         = []
Incomes_source  = []
Expenses        = []
Expenses_source = []

while True:
    print("Total Balance ", Balance)
    print("Type 1 for add income ")
    print("Type 2 for add expense ")
    print("Type 3 for check income ")
    print("Type 4 for check expense ")
    print("Type 5 for exit ")

    choice = int(input("Enter "))    


    if choice == 1:
        Income, source      = input("Enter Income and source seperate by space ").split(maxsplit=1)
        Income              = int(Income)
        source              = str(source)
        Incomes.append(Income)
        Incomes_source.append(source)
        Balance            += Income
        print(Balance)

    elif choice == 2:
        Expense, source         = input("Enter Income and source seperate by space ").split(maxsplit=1)
        Expense                 = int(Expense)
        source                  = str(source)
        Expenses.append(Expense)
        Expenses_source.append(source)
        Balance                -= Expense
        print(Balance)

    elif choice == 3:
        for i,(income,src) in enumerate(zip(Incomes, Incomes_source),start=1):
            print(f"{i}. {income} B from {src}")

    elif choice == 4:
        for i,(expense,src) in enumerate(zip(Expenses, Expenses_source),start=1):
            print(f"{i}. {expense} B from {src}")

    else:
        break


