class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"
        self.attempts = 0

    def check_pin(self):
        pin_entry = input("Enter your 4-digit PIN: ")
        if pin_entry == self.pin:
            print("PIN is correct. You can proceed.")
            return True
        else:
            print("Incorrect PIN. Try again.")
            self.attempts += 1
            if self.attempts < 3:
                self.check_pin()
            else:
                print("You have exceeded the maximum number of attempts. Your card has been blocked.")
                exit()

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        print(f"Deposit successful. Your new balance is: ${self.balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient funds. Please try again.")
            self.withdraw()
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def main_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        self.check_pin()
        self.main_menu()


if __name__ == "__main__":
    atm = ATM(1000)
    atm.run()