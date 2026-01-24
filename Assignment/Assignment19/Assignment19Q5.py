from functools import reduce

def isPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def main():
    arr = [2, 70, 11, 10, 17, 23, 31, 77]

    fdata = list(filter(isPrime, arr))
    print("List after filter:", fdata)

    mdata = list(map(lambda no: no * 2, fdata))
    print("List after map:", mdata)

    rdata = reduce(lambda a, b: a if a > b else b, mdata)
    print("Output of reduce:", rdata)

if __name__ == "__main__":
    main()
