
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_details(self):
        return f"Thank you, {self.__age} years old, {self.__name.title()}"


class Bank(User):
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of: ${round(self.balance, 2)}"

    def deposit(self):
        dp = float(input(f"{self.name.title()}, please enter how much you would like to deposit? "))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        return f"Your balance is now: {round(self.balance, 2)}"

    def withdraw(self):
        wd = float(input(f"{self.name.title()}, please enter how much you would like to withdraw? "))
        if self.balance < wd:
            return "You can't withdraw that amount"
        else:
            print("Thank you for withdrawing...")
            self.balance -= wd
            self.total_withdraws += 1

def options(user_one_bank, user_two_bank=None):
    print("Thank you for creating your bank account")
    print("Here are a list of options, please choose the number you want")
    while True:
        options_choice = int(input("""1) See Balance \n2) Withdraw \n3) Deposit
        \n4) See Total Widthraws \n5) See Total Deposits \n6) Quit\n"""))
        if options_choice == 1:
            print(user_one_bank.show_info())
            if options_choice == 1 and user_two_bank is not None:
                print(user_two_bank.show_info())
        elif options_choice == 2:
            print(user_one_bank.withdraw())
            if options_choice == 2 and user_two_bank is not None:
                wd = input(f"{user_two_bank.name} Would you like to withdraw? Yes or No: ")
                if wd.lower() == "yes":
                    print(user_two_bank.withdraw())