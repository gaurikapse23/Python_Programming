filename = input("Enter file name: ")

with open(filename, "r") as f:
    for line in f:
        print(line.strip())
