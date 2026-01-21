def CheckPrime(No):
    for i in range(2,No):
        if((No % i) == 0):
            return False
        else:
            return True

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int (input())

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("It is Prime")
    else:
        print("It is not Prime")    

    
if __name__ == "__main__":
    main()    