def SumationOfDigit(no):
    sum = 0
    for digit in str(no):
        sum = sum + int(digit)
    
    print("Sum is :",sum)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = SumationOfDigit(Value)
    
if __name__ == "__main__":
    main()