import threading

def isPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(arr):
    print("Prime numbers:")
    for no in arr:
        if isPrime(no):
            print(no)

def NonPrime(arr):
    print("Non-prime numbers:")
    for no in arr:
        if not isPrime(no):
            print(no)

def main():
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 11]

    t1 = threading.Thread(target=Prime, args=(arr,))
    t2 = threading.Thread(target=NonPrime, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
