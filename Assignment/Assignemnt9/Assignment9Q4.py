def Cube(no):
    return no * no * no

def main():
    Value = 0
    result = 0
  
    print("Enter number : ")
    Value = int (input())

    result = Cube(Value)

    print("Cube is : ",result)
    
if __name__ == "__main__":
    main()
