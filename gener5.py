def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Generate and print the countdown from 5 to 0
for num in countdown(5):
    print(num)