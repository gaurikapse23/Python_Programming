
Addition = lambda No1 ,No2 : No1 + No2 

def main():
    Value1 = 0
    Value2 = 0
    Ret = False

    print("Enter number : ")
    Value1 = int(input())

    print("Enter number : ")
    Value2 = int(input())

    Ret = Addition(Value1 , Value2)

    print("It Addition is : ",Ret)
    
if __name__ == "__main__":
    main()