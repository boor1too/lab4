def even_generator(N):
    for i in range(0, N+1, 2):
        yield i

# Get the value of N from the console
N = int(input("Enter a number: "))

# Generate the even numbers up to N
even_numbers = even_generator(N)

# Print the even numbers in a comma-separated format
print(*even_numbers, sep=',')