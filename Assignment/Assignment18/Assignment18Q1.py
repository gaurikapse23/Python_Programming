def AddList(arr):
    total = 0
    for no in arr:
        total += no
    return total

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    print("Output:", AddList(arr))

if __name__ == "__main__":
    main()
