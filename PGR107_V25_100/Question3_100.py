#PGR107
#Kandidatnr: 100
#Question 3

class Menu:
    def __init__(self):
        self.options = [
            "Open a new account",
            "Deposit money into your account",
            "Withdraw money from your account",
            "Add interests to the current balance",
            "Get the current balance of your account",
            "Quit"
        ]

    def add_option(self, option):
        self.options.append(option)

    def get_input(self):
        print("Bank Menu:")
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx} {option}")
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= len(self.options):
                return choice
            else:
                print("Invalid option. Please try again.")
                return self.get_input()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_input()


class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be more than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be more than 0.")
        elif amount > self.balance:
            print(f"You dont have enough funds. Your current balance is: ${self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    def add_interest(self, rate=0.02):
        interest = self.balance * rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} added at {rate*100:.1f}% rate.")

    def get_balance(self):
        return self.balance


def main():
    menu = Menu()
    account = None

    while True:
        choice = menu.get_input()

        if choice == 1:
            account = BankAccount()
            print("New bank account created.")
        elif choice == 2:
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("You need to open an account first.")
        elif choice == 3:
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("You need to open an account first.")
        elif choice == 4:
            if account:
                account.add_interest()
            else:
                print("You need to open an account first.")
        elif choice == 5:
            if account:
                print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("You need to open an account first.")
        elif choice == 6:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
