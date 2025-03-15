from MulTableExcp import ZeroError, NegNumberError


try:
    n = int(input("Enter a number: "))  # Ensure integer input
    table()
except (ValueError, ZeroError, NegNumberError) as e:
    if isinstance(e, ValueError):
        print("\tDon't enter alphanumeric characters, strings, or special symbols.")
    elif isinstance(e, ZeroError):
        print("\tDon't enter zero.")
    elif isinstance(e, NegNumberError):
        print("\tDon't enter negative numbers.")