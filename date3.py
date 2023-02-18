from datetime import datetime

# Get the current date and time with microseconds
now = datetime.now()

# Drop the microseconds from the current date and time
now_without_microseconds = now.replace(microsecond=0)

# Print the result in a human-readable format
print("Current date and time with microseconds:", now)
print("Current date and time without microseconds:", now_without_microseconds)