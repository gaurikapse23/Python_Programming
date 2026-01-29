class BankAccount:
    ROI = 10.5   # Class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        money = float(input("Enter amount to deposit: "))
        self.Amount += money

    def Withdraw(self):
        money = float(input("Enter amount to withdraw: "))
        if money <= self.Amount:
            self.Amount -= money
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

def main():
    obj1 = BankAccount("Gauri", 10000)

    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()

    obj1.Display()
    print("Interest:", obj1.CalculateInterest())

if __name__ == "__main__":
    main()
