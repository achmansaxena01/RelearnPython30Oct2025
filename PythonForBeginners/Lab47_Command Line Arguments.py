import sys

# Validate correct argument count
if len(sys.argv) <= 2:
    print("Usage: python atm.py <option> [amount]")
    print(" 1 . Check balance"
          "\n 2 . Withdraw amount"
          "\n 3 . Deposit amount with cash"
          "\n 4 . Deposit amount with check")
    sys.exit()

ActBalance = 10000
option = None
amount = None

# Validate and parse option
try:
    option = int(sys.argv[1])
except ValueError:
    print("Option must be a number")
    sys.exit()

# Parse amount if provided
if len(sys.argv) >= 3:
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("Amount must be a number")
        sys.exit()

match option:
    case 1:
        print("You have selected the option to check Balance : ")
        print(f"Balance : {ActBalance}")
    case 2:
        print("You have selected the option to withdraw amount : ")
        if amount is None:
            print("Please enter a valid input")
        elif 0 < amount <= ActBalance:
            ActBalance -= amount
            print(f"Withdrew amount : {amount}")
            print(f"Remaining Balance : {ActBalance}")
        else:
            print("Please enter a valid amount which is less than the balance")
    case 3:
        print("You have selected the option to Deposit amount by cash: ")
        if amount is None:
            print("Please enter a valid input")
        else:
            ActBalance += amount
            print(f"Deposit amount : {amount}")
            print(f"Remaining Balance : {ActBalance}")
    case 4:
        print("You have selected the option to Deposit amount by check :")
        if amount is None:
            print("Please enter a valid input")
        else:
            ActBalance += amount
            print(f"Deposit amount : {amount}")
            print(f"Remaining Balance : {ActBalance}")
    case _:
        print("Please enter a valid command")
