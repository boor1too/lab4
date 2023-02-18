from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Subtract five days from the current date
five_days_ago = now - timedelta(days=5)

# Print the result in a human-readable format
print("Current date and time:", now)
print("Five days ago:", five_days_ago)