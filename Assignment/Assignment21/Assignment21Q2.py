import threading

def Maximum(arr):
    print("Maximum element:", max(arr))

def Minimum(arr):
    print("Minimum element:", min(arr))

def main():
    size = int(input("Enter number of elements: "))
    arr = []

    for i in range(size):
        arr.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(arr,))
    t2 = threading.Thread(target=Minimum, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
