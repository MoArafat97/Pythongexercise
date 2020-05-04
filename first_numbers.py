for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(f"\n{numbers}")

even_numbers = list(range(2, 11, 2))
print(f"\n{even_numbers}")

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
   # squares.append(value ** 2)

print(squares)



