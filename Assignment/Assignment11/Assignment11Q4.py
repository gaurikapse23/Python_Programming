def ReverseNumber(no):
    rev = 0
    for i in str(no):
        rev = rev * 10 + no % 10
        no //= 10
    
    print("Reverse is :",rev)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = ReverseNumber(Value)
    
if __name__ == "__main__":
    main()