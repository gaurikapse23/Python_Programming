def ChkFactorial(no):
    Fact = 1
    for i in range(1,no + 1):
        Fact = Fact * i
    
    print("Factorial is:",Fact)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = ChkFactorial(Value)
    
if __name__ == "__main__":
    main()
