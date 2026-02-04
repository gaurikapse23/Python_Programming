filename = input("Enter file name: ")

with open(filename, "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))
