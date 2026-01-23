from functools import reduce

def main():
    numbers = [1,2,3,4,5,6]
    addition = reduce(lambda no1 , no2: no1 + no2, numbers)
    print("Addition : ",addition)

if __name__ == "__main__":
    main()