def Sumation(no):
    sum = 0
    for i in range(1,no + 1):
        sum = sum + i
    
    print("Sum is :",sum)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = Sumation(Value)
    
if __name__ == "__main__":
    main()
