from functools import reduce

def main():
    numbers = [10,15,20,30,45,50]
    result = list(filter(lambda no : no % 3 == 0 and no % 5 == 0, numbers))
    print("Division by 3 and 5 : ",result)

if __name__ == "__main__":
    main()