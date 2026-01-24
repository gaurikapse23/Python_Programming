from functools import reduce

def main():
    arr = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    fdata = list(filter(lambda no: no % 2 == 0, arr))
    print("List after filter:", fdata)

    mdata = list(map(lambda no: no * no, fdata))
    print("List after map:", mdata)

    rdata = reduce(lambda a, b: a + b, mdata)
    print("Output of reduce:", rdata)

if __name__ == "__main__":
    main()
