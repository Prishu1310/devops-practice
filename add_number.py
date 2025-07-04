def add_two_numbers():
    """
    Prompts the user for two numbers, calculates their sum,
    and prints the result.
    """
    print("--- Simple Addition Program ---")

    try:
        # Get the first number from the user
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str) # Convert input to a float to handle decimals

        # Get the second number from the user
        num2_str = input("Enter the second number: ")
        num2 = float(num2_str) # Convert input to a float

        # Calculate the sum
        sum_result = num1 + num2

        # Display the result
        print(f"\nThe sum of {num1} and {num2} is: {sum_result}")

    except ValueError:
        # Handle cases where the user enters non-numeric input
        print("\nInvalid input. Please enter valid numbers only.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# Call the function to run the program
if __name__ == "__main__":
    add_two_numbers()
