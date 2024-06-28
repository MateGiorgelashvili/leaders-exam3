class bAccount:
    def __init__(self, account_id, account_name, balance=0):
        self.account_id = account_id
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"თქვენ შეიტანეთ ${amount}, ამჟამინდელი ბალანსი: ${self.balance}")
        else:
            print("თანხის შესატანად მინიმალური თანხა 1 ლარია.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"თქვენ ჩამოგეჭრათ ${amount} ანგარიშის ნომრიდან. ამჟამინდელი ბალანსი: ${self.balance}")
        else:
            print("თქვენს ანგარიშზე არარის ხელმისაწვდომი თანხა")

    def get_balance(self):
        return self.balance

    def get_details(self):
        return f"ანგარიშის ნომერი: {self.account_id}, ანგარიშის მფლობელი: {self.account_name}, ბალანსი: {self.balance}"

    def del_acc(self):
        self.account_id = None
        self.account_name = None
        self.balance = 0
        print("ექაუნთი წაშლილია")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def register(self, account_id, account_name):
        if account_id not in self.accounts:
            self.accounts[account_id] = bAccount(account_id, account_name)
            print(f"თქვენ დარეგისტრირდით წარმატებით {account_name}. თქვენი ანგარიშის ნომერია {account_id}")
        else:
            print("ანგარიში ამ ნომრით უკვე არსებობს")

    def get_acc(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            print("ანგარიში ვერ მოიძებნა")
            return None

    def get_all_accounts(self):
        print(f"ექაუნთები {self.name}-ში:")
        for account in self.accounts.values():
            print(account.get_details())

    def delete_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print(f"ანგარიში {account_id} წაიშალა.")
        else:
            print("ანგარიში ვერ მოიძებნა")


if __name__ == "__main__":
    bank = Bank("Dragon Bank")
    account_counter = 1
    while True:
        print("მოგესალმებით Dragon Bank-ში")
        print("აირჩიეთ:\n 1. ექაუნთის შექმნა\n 2. დეპოზიტი\n 3. გამოტანა\n 4. ანგარიშის წაშლა\n 5. ექაუნთის მოძიება\n 6. ყველა ანგარიში\n 7. გათიშვა")
        user_choice = int(input("შეიყვანე რიცხვი: "))

        if user_choice == 1:
            account_name = input("შეიყვანე სახელი: ")
            bank.register(account_counter, account_name)
            account_counter += 1

        elif user_choice == 2:
            account_id = int(input("შეიყვანე ექაუნთის ნომერი: "))
            amount = float(input("შეიყვანე თანხა: "))
            account = bank.get_acc(account_id)
            if account:
                account.deposit(amount)

        elif user_choice == 3:
            account_id = int(input("შეიყვანე ექაუნთის ნომერი: "))
            amount = float(input("შეიყვანე თანხა: "))
            account = bank.get_acc(account_id)
            if account:
                account.withdraw(amount)

        elif user_choice == 4:
            account_id = int(input("შეიყვანე ექაუნთის ნომერი: "))
            bank.delete_account(account_id)

        elif user_choice == 5:
            account_id = int(input("შეიყვანე ექაუნთის ნომერი: "))
            account = bank.get_acc(account_id)
            if account:
                print(account.get_details())

        elif user_choice == 6:
            bank.get_all_accounts()

        elif user_choice == 7:
            print("გათიშვა")
            break

        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")
