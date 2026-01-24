import threading

def EvenFactor(no):
    total = 0
    print("Even Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            total += i
    print("Sum of even factors:", total)

def OddFactor(no):
    total = 0
    print("Odd Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            total += i
    print("Sum of odd factors:", total)

def main():
    no = int(input("Enter number: "))

    t1 = threading.Thread(target=EvenFactor, args=(no,))
    t2 = threading.Thread(target=OddFactor, args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
