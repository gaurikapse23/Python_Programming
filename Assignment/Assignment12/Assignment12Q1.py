def ChkVowel(ch):
    if ch in ('a','e','i','o','u'):
        print("Vowel")
    else:
        print("Consonant")    

def main():
    print("Enter character : ")
    Value = str(input())

    ChkVowel(Value)

if __name__  == "__main__":
    main()        