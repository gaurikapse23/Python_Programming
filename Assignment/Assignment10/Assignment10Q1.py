def Multiplication(no):
    for i in range(1,11):
        print(no * i , end =" ")
    
    return no

def main():
   
    print("Enter number : ")
    Value = int (input())

    result = Multiplication(Value)
    
if __name__ == "__main__":
    main()
