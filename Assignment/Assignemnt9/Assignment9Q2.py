def ChkGreater(no1 , no2):
    if no1 > no2:
        print("No1 is greater")
    else:
        print("No2 is greater")

def main():
    Value1 = 0
    Value2 = 0

    print("Enter first number : ")
    Value1 = int (input())

    print("Enter second number : ")
    Value2 = int (input())

    ChkGreater(Value1,Value2)
    
if __name__ == "__main__":
    main()
