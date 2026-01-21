def AreaOfRectAngel(length,width):
    return length * width

def main():

    Ret = 0 

    print("Enter length : ")
    Value1 = float(input())

    print("Enter width : ")
    Value2 = float(input())

    Ret = AreaOfRectAngel(Value1 , Value2)

    print("Area of rectangle : ",Ret)

if __name__  == "__main__":
    main()        