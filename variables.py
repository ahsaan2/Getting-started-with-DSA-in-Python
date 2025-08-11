message = "hello world!"
print(message)
message = 2  # re-assigned
# that means python is dynamically typed language. We don't have to declare the variable type.
print(message)
# myVariable  -> camel case (usually in java)
# my_variable_name -> snake case (usually used in python)
# MyVariableName -> pascal case -> every word starts with a capital letter.

# -------Multipla Assignments--------------
#  Python allows you to assign multiple variables in a single line. just separate the variables with comma
# msg1, msg2, msg3 = "message1", "message2", "message3"
# number of variables should match
# print(msg1)
msg1 = "re_assign message 1"
print(msg1)

# // we can swap the two messages in a single line also

var1 = 14
var2 = 15
print("before swapping the number", var1, var2)
var1, var2 = var2, var1
# assign var1 as var2 and var2 as var1
print(var1, var2)

msg1, msg2 = "world", "hello"
msg3, msg4, msg5 = "Name", "is", "My"
# output should be "hello world My name is"

#msg1 -> msg2, msg2 -> msg1, msg3 -> msg5, ,msg4 -> msg3, ,msg5 -> msg4
msg1, msg2, msg3, msg4, msg5 = msg2, msg1, msg5, msg3, msg4
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

# variables types
integer_type = 12
temperature = 98.2 # floating points
bool_type = True
name = "<NAME>"
my_list = [1, 2, 3]  # these are sequence of values

# getting the type of the variable
print(type(integer_type))  # int
print(type(temperature))
print(type(bool_type))  # bool

# -------------------------Dynamic Typing------------------------------------
# the type of the single variable can change, we can change the variable from string to integer
# and vice-versa

# here the type of the variable's are decided at the runtime
print("python dynamic typed variables")
integer_variable = 10
print(type(integer_variable))
integer_variable = "Ahsaan"
print(type(integer_variable))
integer_variable = [1, 2, 3]
print(type(integer_variable))


# ---------------Type Casting---------------------------------
# once datatype to another
integer_variable = 10.9  # float
# to convert this to integer, we use int, and it strips everything past the floating point
print("we are type casting here", int(integer_variable))

type_cast = int(integer_variable)
print("Here we will have the type_cast as int", type(type_cast))

print("we are still getting float here", type(integer_variable))


# we can create string to integer, when the string itself has the number
variableInteger = "1212"
print(type(variableInteger))  # string
var2 = int(variableInteger)
print("should be a integer", type(var2))
# print(type(variableInteger))


# -------------------Empty Variable-----------------
# none in java , None in python
# None indicates the absence of the value
var  = None
print(type(var))  # NoneType

# ------------------------------------------------Arithemetic Operators-------------
x , y = 2, 4
x, y = y, x
print(x + y)
print(x - y)
a = 10
b = 12
print(a / b)
print(a % b)

# // floor division -->> divides the first operand by the second and rounds down the result to and integer

a = 20
b = 10
print(a / b)  # 2.0
print("FloorDivision is ", a // b)  # 2
# Exponential ** raises the first operand to the power of the second operand
print("Exponential is ", a ** 3)



# --------Boolean------
# Logical OR
a = True
b = False
print("If either is true, we have true:-", a or b)

print("If both are true only then And is true:-", a and b)
print("Logical not:-", not a)  # false
