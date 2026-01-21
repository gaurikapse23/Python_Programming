def ChkPalindrome(No):
    original = str(No)
    rev = ""
    for i in original:
        rev = i+rev
    return original == rev    

def main():
    print("Enter number : ")
    Value = int (input())

    if ChkPalindrome(Value):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")    

    
if __name__ == "__main__":
    main()    