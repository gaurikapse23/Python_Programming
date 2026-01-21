def ChkFactorial(no):

    for i in range(1,no + 1,2):
        print(i)

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = ChkFactorial(Value)
    
if __name__ == "__main__":
    main()
