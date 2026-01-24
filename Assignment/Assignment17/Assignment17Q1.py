def Addition(Value1 , Value2):
    Ans = 0 
    Ans = Value1 + Value2
    return Ans

def Substraction(Value1 , Value2):
    Ans = 0 
    Ans = Value1 - Value2
    return Ans

def Multiplication(Value1 , Value2):
    Ans = 0 
    Ans = Value1 * Value2
    return Ans

def Division(Value1 , Value2):
    Ans = 0 
    Ans = Value1 / Value2
    return Ans

def main():

    No1 = 0 
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = Addition(No1 , No2)
    print("Addition is :" , Result)

    Result = Substraction(No1 , No2)
    print("Substraction is :" , Result)

    Result = Multiplication(No1 , No2)
    print("Multiplication is :" , Result)

    Result = Division(No1 , No2)
    print("Division is :" , Result)
    
if __name__ == "__main__":
    main()


