def positional_greeting(name, message):
    print("Positional:", message, name)


def keyword_greeting(name, message):
    print("Keyword:", message, name)


def default_greeting(name="Student"):
    print("Default: Hello", name)


def calculate_total(*numbers):
    return sum(numbers)


positional_greeting("Harini", "Hello")

keyword_greeting(message="Hello", name="Harini")

default_greeting()
default_greeting("Harini")

total = calculate_total(10, 20, 30, 40)
print("Total:", total)
