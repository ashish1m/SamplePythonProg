def exit_prog():
    print("Thank you for using the ATM")
    exit(0)


print("Welcome to the ATM")

while True:
    isCardInserted = input("Please insert the card(Y / N): ")
    if isCardInserted.lower() == 'y':
        break

    if isCardInserted.lower() == 'x':
        exit_prog()

balance = 10000
chances = 3

while chances > 0:
    pin = int(input("Please enter your four digit pin: "))
    if pin == 1234:
        # TODO
        pass
    else:
        chances -= 1
        if chances == 0:
            print("No more tries. Please come back after 24 hrs.")
            break
        print("Incorrect pin. Try again.")
exit_prog()
