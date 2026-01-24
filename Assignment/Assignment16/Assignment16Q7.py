def DivisibleByFive(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter number: "))
    print(DivisibleByFive(no))

if __name__ == "__main__":
    main()
