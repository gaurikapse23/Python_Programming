import sys

source = sys.argv[1]
destination = "Demo.txt"

with open(source, "r") as src:
    data = src.read()

with open(destination, "w") as dest:
    dest.write(data)

print("Contents copied to Demo.txt")
