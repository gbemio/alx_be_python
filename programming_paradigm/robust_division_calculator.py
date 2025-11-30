def safe_divide(numerator, denominator):
    """
    Perform division safely, handling errors for non-numeric inputs and division by zero.
    Returns a string message with either the result or an error.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
