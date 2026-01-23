from functools import reduce

def main():
    numbers = [1,2,3,4,5,6,7,8]
    even_count = len(list(filter(lambda no : no % 2 == 0, numbers)))
    print("Product : ",even_count)

if __name__ == "__main__":
    main()