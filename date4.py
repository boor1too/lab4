from datetime import datetime

# Define two dates to compare
date1 = datetime(2023, 2, 15, 12, 0, 0)
date2 = datetime(2023, 2, 16, 12, 0, 0)

# Calculate the difference between the two dates in seconds
difference = (date2 - date1).total_seconds()

# Print the result in a human-readable format
print("The difference between", date1, "and", date2, "is", difference, "seconds.")