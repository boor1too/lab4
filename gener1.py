def square_generator(N):
    for i in range(1, N+1):
        yield i**2

# Generate the squares of numbers up to 5
for square in square_generator(5):
    print(square)

# Generate a list of the squares of numbers up to 10
squares = [x**2 for x in square_generator(10)]
print(squares)