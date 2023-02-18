from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Calculate the dates for yesterday, today, and tomorrow
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

# Print the results in a human-readable format
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", now.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))