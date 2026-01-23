from functools import reduce

def main():
    string = ["Python","Java","Ai","LB","PPA"]
    result = list(filter(lambda no : len(no) > 5 , string))
    print("String with length > 5 : ",result)

if __name__ == "__main__":
    main()