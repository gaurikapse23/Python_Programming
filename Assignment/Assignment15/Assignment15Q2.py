from functools import reduce

def main():
    numbers = [1,2,3,4,5,6]
    even_number = list(filter(lambda no : no % 2 == 0 , numbers))
    print("Even numbers : ",even_number)

if __name__ == "__main__":
    main()