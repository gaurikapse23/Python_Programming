def CountDigits(No):
    Count = 0
    while No > 0:
        Count += 1
        No //= 10
    print("Count of digits : ",Count)
    
def main():
    print("Enter number : ")
    Value = int (input())

    Ret = CountDigits(Value)
    
if __name__ == "__main__":
    main()    