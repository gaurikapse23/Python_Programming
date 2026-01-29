class Numbers:
    def __init__(self):
        self.Value = int(input("Enter number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.SumFactors() - self.Value == self.Value:
            return True
        return False

def main():
    obj = Numbers()

    print("Prime:", obj.ChkPrime())
    obj.Factors()
    print("Sum of Factors:", obj.SumFactors())
    print("Perfect Number:", obj.ChkPerfect())

if __name__ == "__main__":
    main()
