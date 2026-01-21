def ChkFactorial(no):
    for i in range(1,no + 1):
        if no % i == 0:
            print("Factorial is:",i)

def main():
   
    print("Enter number : ")
    Value = int (input())

    ChkFactorial(Value)
    
if __name__ == "__main__":
    main()