def BinaryEquivalent(no):
    return bin(no).replace("0b","")

def main():

    Ret = 0 

    print("Enter number : ")
    Value = int(input())

    Ret = BinaryEquivalent(Value)

    print("Binary Equivalent : ",Ret)

if __name__  == "__main__":
    main()        