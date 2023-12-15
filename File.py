# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for _ in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Number of Fibonacci numbers to generate
n = 20
# Here is im on branch main

# Generate and print the first 20 Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)
print("First", n, "Fibonacci numbers:", fibonacci_numbers)
