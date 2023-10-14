def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0


def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"


def main():
    """Main function."""
    number1 = 10
    number2 = 20
    result = calculate_sum(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}.")

    number3 = 15
    if is_even(number3):
        print(f"{number3} is even.")
    else:
        print(f"{number3} is odd.")

    person = "Alice"
    greeting = greet(person)
    print(greeting)


if __name__ == "__main__":
    main()
