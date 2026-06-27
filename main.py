
class Atm:
    def __init__(self):
        self.money = 00.00

    def deposit_money(self):

        while True:
            try:
                amount = float(input("enter the amount you want to deposit : "))
            except ValueError:
                print("enter a valid number ")
                continue
            if amount > 0:
                self.money += amount
                print(f"{amount}$ has been deposited to your account")
                print(f"your balance is : {self.money:.2f}")
                break

            else:
                print("amount cant be negative or 0 ")


    def withdraw_money(self):
        while True:
            try:
                amount= float(input("enter the amount you want to withdraw : "))
            except ValueError:
                print("enter a valid number ")
                continue
            if amount > 0:
                if amount > self.money :
                    print("Insufficient balance")

                else:
                    self.money -= amount
                    print(f"{amount}$ has been withdrawn from your account")
                    print(f"your balance is : {self.money:.2f}")
                    break
            else:
                print("amount cannot be negative or 0")


    def view_balance(self):
        print(f"{self.money}$ is your account balance ")


def main():
    a = Atm()
    while True:

        ask = input("what you want to do \n1.deposit money \n2.withdraw money \n3.view balance \n4.exit : ").strip().lower()
        if ask == "1" :
            a.deposit_money()
        elif ask == "2":
            a.withdraw_money()
        elif ask == "3" :
            a.view_balance()
        elif ask == "4" :
            print("bye!")
            break
        else:
            print("give a choice between 1, 2,3 ,4 ")

main()