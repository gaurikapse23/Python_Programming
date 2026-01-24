def SumDigits(no):
    total = 0
    while no > 0:
        total += no % 10
        no //= 10
    return total

def main():
    no = int(input("Enter number: "))
    print("Addition of digits:", SumDigits(no))

if __name__ == "__main__":
    main()
