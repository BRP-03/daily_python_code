
# Project Name: Even/Odd Checker
# File: even_odd_checker.py

# This Python project is a simple command-line tool that checks if a user-entered
# number is Even or Odd. It's designed to be beginner-friendly, with clear
# comments and basic error handling.

# --- 1. Function to check Even or Odd ---
def check_even_odd(number):
    """
    Checks if a given integer is even or odd.

    Args:
        number (int): The integer number to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
             Returns "Invalid" if input is not an integer (though this is
             handled by the main loop's try-except block).
    """
    # The modulo operator (%) returns the remainder of a division.
    # If a number is perfectly divisible by 2, its remainder will be 0.
    # Numbers with a remainder of 0 when divided by 2 are Even.
    # Numbers with a remainder of 1 (or -1 for negative odds) are Odd.
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# --- 2. Main Program Logic ---
# The 'if __name__ == "__main__":' block ensures that the code inside it
# only runs when the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    print("-----------------------------------")
    print("  Welcome to the Even/Odd Checker! ")
    print("-----------------------------------")
    print("Enter an integer to check, or type 'q' to quit.")

    # Start an infinite loop to allow the user to check multiple numbers
    while True:
        # Prompt the user to enter a number
        # The input() function reads a line from input and returns it as a string.
        user_input = input("\nEnter a number (or 'q' to quit): ")

        # Check if the user wants to quit the program
        # .lower() converts the input string to lowercase to handle 'Q', 'q', 'Quit', etc.
        if user_input.lower() == 'q':
            print("Thanks for using the Even/Odd Checker. Goodbye!")
            break  # Exit the 'while' loop, ending the program

        # --- 3. Input Validation and Error Handling ---
        # Use a try-except block to gracefully handle potential errors,
        # especially when converting user input (which is always a string) to an integer.
        try:
            # Attempt to convert the user's input string into an integer.
            # If the user enters something that cannot be converted (e.g., "hello", "3.14"),
            # int() will raise a ValueError.
            number = int(user_input)

            # If the conversion is successful, call our check_even_odd function
            # with the valid integer.
            result = check_even_odd(number)

            # Print the result to the user using an f-string for easy formatting.
            print(f"The number {number} is {result}.")

        except ValueError:
            # This block runs if int(user_input) fails (i.e., user entered non-integer text).
            print("Invalid input. Please enter a whole number (integer) or 'q' to quit.")
        except Exception as e:
            # This is a general catch-all for any other unexpected errors,
            # which is good practice for robust programs.
            print(f"An unexpected error occurred: {e}")

    print("\nProgram finished.")
