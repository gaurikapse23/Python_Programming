largest = lambda no1 ,no2 , no3: no1 if (no1 > no2 and no1 > no3)else(no2 if no2 > no3 else no3)

def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    print("Enter second number : ")
    Value3 = int(input())

    Ret = largest(Value1 , Value2 , Value3)

    print("largest is : ",Ret)
    
if __name__ == "__main__":
    main()