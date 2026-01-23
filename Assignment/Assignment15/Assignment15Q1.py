from functools import reduce

numbers = [1,2,3,4,5]

square = list(map(lambda no : no * no , numbers))
print(square)