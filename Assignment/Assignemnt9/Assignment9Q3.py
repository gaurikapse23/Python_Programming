def Square(no):
    return no * no

def main():
    Value = 0
    result = 0
  
    print("Enter number : ")
    Value = int (input())

    result = Square(Value)

    print("Square is : ",result)
    
if __name__ == "__main__":
    main()
