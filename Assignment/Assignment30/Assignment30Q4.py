source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as src:
    data = src.read()

with open(destination, "w") as dest:
    dest.write(data)

print("File copied successfully")
