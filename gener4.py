def squares(a, b):
    for i in range(a, b+1):
        yield i**2

# Generate and print the squares of the numbers from 1 to 5
for square in squares(1, 5):
    print(square)