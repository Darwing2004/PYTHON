class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = float(balance)  # balance en nombre (float)

    def deposit(self):
        money = float(input("How many do you want to add? : "))
        self.balance += money
        print(f"{money} added to your account. New balance: {self.balance}")

    def withdraw(self):
        money = float(input("How much do you want to withdraw? : "))
        if money > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= money
            print(f"You have withdrawn {money}. New balance: {self.balance}")

    def display_balance(self):
        print(f"You have {self.balance} in your account.")


# Création de l'objet
Dada_account = BankAccount("Darwing", "Degni", 1042004, "Student Account", 104, 100)

Dada_account.deposit()
Dada_account.withdraw()
Dada_account.display_balance()
