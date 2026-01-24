def Frequency(arr, no):
    count = 0
    for i in arr:
        if i == no:
            count += 1
    return count

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    search = int(input("Enter element to search: "))
    print("Output:", Frequency(arr, search))

if __name__ == "__main__":
    main()
