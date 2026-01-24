def Maximum(arr):
    max_no = arr[0]
    for no in arr:
        if no > max_no:
            max_no = no
    return max_no

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    print("Output:", Maximum(arr))

if __name__ == "__main__":
    main()
