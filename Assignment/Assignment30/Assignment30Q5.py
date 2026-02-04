filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, "r") as f:
    data = f.read()

if word in data:
    print(f'Word "{word}" is found in {filename}')
else:
    print(f'Word "{word}" is not found in {filename}')
