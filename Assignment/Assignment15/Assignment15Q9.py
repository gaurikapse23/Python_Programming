from functools import reduce

def main():
    numbers = [1,2,3,4,5]
    product = reduce(lambda no1 , no2: no1 * no2, numbers)
    print("Product : ",product)

if __name__ == "__main__":
    main()