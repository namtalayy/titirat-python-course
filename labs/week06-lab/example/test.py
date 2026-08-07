""""""
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Calling the function
print("Calling say_hello():")
say_hello()
print()
""""""
""""""
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()
""""""
# Example 3: Using returned values in expressions
def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def square(n):
    """Returns the square of a number"""
    return n * n

print("Using return values in expressions:")
result = multiply(4, 5) + square(3)
print(f"multiply(4, 5) + square(3) = {multiply(4, 5)} + {square(3)} = {result}")
print()