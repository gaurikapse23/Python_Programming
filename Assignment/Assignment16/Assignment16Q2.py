def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    no = int(input("Enter number: "))
    ChkNum(no)

if __name__ == "__main__":
    main()
