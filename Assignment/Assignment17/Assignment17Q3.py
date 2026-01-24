def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact *= i
    return fact

def main():
    no = int(input("Enter number: "))
    print("Factorial:", Factorial(no))

if __name__ == "__main__":
    main()
