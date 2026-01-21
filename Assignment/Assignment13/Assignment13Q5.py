def DisplayGrade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "first class"
    elif marks >= 50:
        return "Second class"
    else:
        return "fail"

def main():

    Ret = 0 

    print("Enter marks : ")
    Value = int(input())

    Ret = DisplayGrade(Value)

    print("Grade : ",Ret)

if __name__  == "__main__":
    main()        