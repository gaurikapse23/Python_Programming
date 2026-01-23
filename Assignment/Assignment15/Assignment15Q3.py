from functools import reduce

def main():
    numbers = [1,2,3,4,5,6]
    Odd_number = list(filter(lambda no : no % 2 != 0 , numbers))
    print("Odd numbers : ",Odd_number)

if __name__ == "__main__":
    main()