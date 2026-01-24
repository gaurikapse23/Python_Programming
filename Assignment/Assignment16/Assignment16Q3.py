def Add(a, b):
    return a + b

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    result = Add(no1, no2)
    print("Addition is:", result)

if __name__ == "__main__":
    main()
