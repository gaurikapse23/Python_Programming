
Division = lambda No : True if (No % 5 == 0) else False

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = Division(Value)

    if(Ret == True):
        print("It is Divided by 5")
    else:
        print("It is not Divided by 5")
    
if __name__ == "__main__":
    main()