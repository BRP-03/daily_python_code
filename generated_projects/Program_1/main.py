
# main.py

# --- Hello World with User Input Project ---
# This script demonstrates how to get input from a user and then use that input
# to display a personalized "Hello World" message.

# Step 1: Greet the user and ask for their name.
# The `input()` function is used to display a prompt to the user and then
# waits for the user to type something and press Enter.
# Whatever the user types is returned as a string and stored in the `user_name` variable.
print("Hello there!")
user_name = input("What is your name? ")

# Step 2: Construct the personalized greeting message.
# We use an f-string (formatted string literal) for easy and readable string formatting.
# The 'f' before the opening quote indicates an f-string.
# Variables enclosed in curly braces `{}` inside an f-string are automatically
# replaced with their values.
greeting_message = f"Hello, {user_name}! Welcome to the Python world!"

# Step 3: Display the personalized greeting to the user.
# The `print()` function is used to output text (or variable values) to the console.
print(greeting_message)

# Step 4: Add a friendly closing message.
print("It's great to have you here!")

# --- End of Project ---
