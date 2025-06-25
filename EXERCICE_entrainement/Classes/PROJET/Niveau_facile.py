# Write code below 💖


class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self):
        money = float(input("How many do you want to add ? :"))
        self.balance += money
        print(f"{money} added to your account ! New balance: {self.balance}")

    def withdraw(self):
        money = 25
        self.balance -= money
        print(f"Vous avez retirer {money} !")

    def display_balance(self):
        print(f"Vous avez {self.balance} dans votre compte")


Dada_account = BankAccount("Darwing", "Degni", 1042004, "Student Account", 104, 96)

Dada_account.deposit()
Dada_account.display_balance()
Dada_account.withdraw()
