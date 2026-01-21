def AreaOfCircle(radius):
    pi = 3.14
    return pi * radius * radius

def main():

    Ret = 0 

    print("Enter radius : ")
    Value = float(input())

    Ret = AreaOfCircle(Value)

    print("Area of rectangle : ",Ret)

if __name__  == "__main__":
    main()        