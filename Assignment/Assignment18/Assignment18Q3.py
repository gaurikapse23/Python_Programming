def Minimum(arr):
    min_no = arr[0]
    for no in arr:
        if no < min_no:
            min_no = no
    return min_no

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    print("Output:", Minimum(arr))

if __name__ == "__main__":
    main()
