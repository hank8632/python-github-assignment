# Ask the user for how many hours they studied today
hours = input("How many hours did you study today? ")
try:
    # Convert the input to a number
    hours = float(hours)

    # Calculate weekly study hours
    weekly_hours = hours * 7

    # Display the result clearly to the user
    print(f"You are on track to study {weekly_hours} hours this week.")
except ValueError:
    # Show an error message if the input is not a number
    print("Please enter a valid number.")
