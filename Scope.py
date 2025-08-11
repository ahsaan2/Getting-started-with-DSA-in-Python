# Scope-> region of a program where a variable is recognized and can be accessed.
# LEGB - Rule
# 1. L-> Local Scope-> variables defined inside a function, and accessible only within that function
# 2. E -> Enclosing Scope -> Applies to nested functions, the inner function can access variables from the outer functions
# 3. G ->  Global Scope -> Variables defined at the top level of a script or module, Accessible through the module.
# 4. B- Built-In Scope -> pythons built in names (len, print, range)


# -------------------Local Scope----------------
def fun() -> None:
    n = 10
    print(n)  # prints n here
    # n is local to this function only


fun()
# print("value of local variable is not accessed here", n)

# -------------------Global Scope----------

x = 12  # accessed anywhere in the program


def new_fun() -> None:
    # x = 11  # if we use x = 11, it shadows the value of x from outer scope and its this value in the function
    print("We can access x in function also", x)


new_fun()
print("We can access x outside the function also", x)


# ----------------------Enclosing Scope---

def outer():
    y = 12

    # print(v)
    def inner():
        print("we can access y in inner function", y)
        # v = 12

    inner()


outer()

# ---------------------
n = 100


def print_local_variable(num: int) -> None:
    print(num)
    # print(num)


print_local_variable(n)  # 100
# print_local_variable(100)  #
print(n)


# ------------------------Default Arguments----------------------

def greet(name="world"):
    print("hello", name)


greet()  # name has a default value as world, and if we do not pass argument here, it will
# take default value as world
greet("Bob")


# if default value is not present, we need to provide the argument

def greet(name, punctation="!") -> None:
    print("Hello", name, punctation)


greet("Bob")


#  ---------------------Comparison Operators ---------------------------
# == Equal to, != not equal to,
# x = 10
# y = 21
# print(x == y)
def check_equal(p, y) -> bool:
    return p == y


print(check_equal(10, 10))
