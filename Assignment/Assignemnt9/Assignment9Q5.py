def CheckDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")    

def main():
    Value = 0
      
    print("Enter number : ")
    Value = int (input())

    CheckDivisible(Value)

if __name__ == "__main__":
    main()
