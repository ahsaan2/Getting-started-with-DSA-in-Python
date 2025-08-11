# functions can store the entire block of code that can be reused multiple times.
# defined by using def keyword, followed by function name and parenthesis with colon:

# In python Indentation is not just for readability, it is mandatory
# it tells python which line of code belong to the function


def greet():
    print("Hello")


def say_goodbye(name="name"):
    print("Goodbye!", name)


greet()  # invoke the function
say_goodbye("ahsaan")


def say_greet(name):
    print("Hello", name)


say_greet("Ahsaan")


# multiple parameters
def greet(name, greeting):
    message = "greetings, " + name + "!"
    print(message)


greet("Ahsaan", "Hello")


# --------return function values
def two_sum(n1, n2):
    return n1 + n2


print(two_sum(12, 12))


def product(num1, num2):
    return num1 * num2


prod = product(2, 10)
print(prod)


# ----------Type Hints---------
# makes code readable, it indicates what type od data the function expects to receive and return.

def add(x: int, y: int) -> int:  # (->) expected return type
    return x + y


print(add(1, 2))


def subtract(x: int, y: int) -> int:
    return y - x


print(subtract(1, 2))


#  Function not returning anything
def not_return(x: int, y: int) -> None:  # Not return anything
    print(x + y)
    # return None
    # return x + y

not_return(1, 2)
