import threading

def Small(s):
    count = sum(1 for ch in s if ch.islower())
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase count:", count)

def Capital(s):
    count = sum(1 for ch in s if ch.isupper())
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase count:", count)

def Digits(s):
    count = sum(1 for ch in s if ch.isdigit())
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit count:", count)

def main():
    s = input("Enter string: ")

    t1 = threading.Thread(target=Small, args=(s,), name="Small")
    t2 = threading.Thread(target=Capital, args=(s,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(s,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
