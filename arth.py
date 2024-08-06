def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Division by zero error"

    print(f"Addition of {a} and {b}: {addition}")
    print(f"Subtraction of {a} and {b}: {subtraction}")
    print(f"Multiplication of {a} and {b}: {multiplication}")
    print(f"Division of {a} and {b}: {division}")

# Get user input for integers
a_int = int(input("Enter an integer value for a: "))
b_int = int(input("Enter an integer value for b: "))
print("\nUsing integers:")
arithmetic_operations(a_int, b_int)

# Get user input for floats
a_float = float(input("\nEnter a float value for a: "))
b_float = float(input("Enter a float value for b: "))
print("\nUsing floats:")
arithmetic_operations(a_float, b_float)
