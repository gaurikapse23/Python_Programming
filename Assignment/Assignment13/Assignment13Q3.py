def CheckPerfect(No):
    Sum = 0
    for i in range(1,No):
        if((No % i) == 0):
            Sum += i
    
    return  Sum == No


def main():
    Value = 0

    print("Enter number : ")
    Value = int (input())

    if CheckPerfect(Value):
        print("It is Perfect")
    else:
        print("It is not Perfect")    

    
if __name__ == "__main__":
    main()     