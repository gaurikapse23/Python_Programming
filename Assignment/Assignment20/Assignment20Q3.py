import threading

def EvenList(arr):
    total = 0
    print("Even elements:")
    for no in arr:
        if no % 2 == 0:
            print(no)
            total += no
    print("Sum of even elements:", total)

def OddList(arr):
    total = 0
    print("Odd elements:")
    for no in arr:
        if no % 2 != 0:
            print(no)
            total += no
    print("Sum of odd elements:", total)

def main():
    arr = [10, 21, 32, 43, 54, 65]

    t1 = threading.Thread(target=EvenList, args=(arr,))
    t2 = threading.Thread(target=OddList, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
