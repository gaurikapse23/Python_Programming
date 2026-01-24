def SumFactors(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total += i
    return total

def main():
    no = int(input("Enter number: "))
    print("Addition of factors:", SumFactors(no))

if __name__ == "__main__":
    main()
