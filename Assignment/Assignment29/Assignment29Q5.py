filename = input("Enter file name: ")
word = input("Enter word: ")

with open(filename, "r") as f:
    data = f.read()

count = data.count(word)
print(f'"{word}" appears {count} times in {filename}')

