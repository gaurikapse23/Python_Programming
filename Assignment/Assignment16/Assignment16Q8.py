def Display(no):
    for i in range(no):
        print("*", end=" ")

def main():
    no = int(input("Enter number: "))
    Display(no)

if __name__ == "__main__":
    main()
