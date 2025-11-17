def get_integer_input(prompt):
    """
    Prompts user for integer input and handles invalid entries.

    Args:
        prompt (str): The message to display to the user

    Returns:
        int: The validated integer input
    """
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput cancelled.")
            raise


def get_integer_in_range(prompt, min_value, max_value):
    """
    Prompts user for an integer within a specific range.

    Args:
        prompt (str): The message to display
        min_value (int): Minimum acceptable value
        max_value (int): Maximum acceptable value

    Returns:
        int: An integer within the specified range
    """
    while True:
        value = get_integer_input(prompt)
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Please enter a number between {min_value} and {max_value}.")
