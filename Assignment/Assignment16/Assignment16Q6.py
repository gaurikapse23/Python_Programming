def Check(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    no = int(input("Enter number: "))
    Check(no)

if __name__ == "__main__":
    main()
