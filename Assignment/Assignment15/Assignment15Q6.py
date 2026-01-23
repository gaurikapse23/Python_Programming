from functools import reduce

def main():
    numbers = [10 , 5, 25 , 15]
    minimum = reduce(lambda no1 , no2: no1 if  no1 < no2 else no2, numbers)
    print("Minimum : ",minimum)

if __name__ == "__main__":
    main()