def CountDigits(no):
    count = 0
    while no > 0:
        count += 1
        no //= 10
    return count

def main():
    no = int(input("Enter number: "))
    print("Number of digits:", CountDigits(no))

if __name__ == "__main__":
    main()
