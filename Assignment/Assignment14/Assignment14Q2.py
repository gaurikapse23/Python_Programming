Cube = lambda No : No * No * No

def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube : ",Ret)
    
if __name__ == "__main__":
    main()