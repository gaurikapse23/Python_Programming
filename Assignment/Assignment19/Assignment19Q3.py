from functools import reduce

def main():
    arr = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    fdata = list(filter(lambda no: no >= 70 and no <= 90, arr))
    print("List after filter:", fdata)

    mdata = list(map(lambda no: no + 10, fdata))
    print("List after map:", mdata)

    rdata = reduce(lambda a, b: a * b, mdata)
    print("Output of reduce:", rdata)

if __name__ == "__main__":
    main()
