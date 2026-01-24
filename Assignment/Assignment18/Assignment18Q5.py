import MarvellousNum

def ListPrime(arr):
    total = 0
    for no in arr:
        if MarvellousNum.ChkPrime(no):
            total += no
    return total

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    print("Output:", ListPrime(arr))

if __name__ == "__main__":
    main()
