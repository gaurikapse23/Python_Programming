filename = input("Enter file name: ")

with open(filename, "r") as f:
    words = f.read().split()

print("Total number of words:", len(words))
