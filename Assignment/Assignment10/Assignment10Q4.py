def Factorial(no):

    for i in range(2,no + 1,2):
        print(i)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = Factorial(Value)
    
if __name__ == "__main__":
    main()
