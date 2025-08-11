# Un-ordered, mutable collection of key-value pairs.
# it's like a real-life dictionary: each word(key) maps to a meaning(value)
# Keys must be immutable types (str, int , tuple)
# values can be any type -> strings, numbers, lists

# using curly-braces
my_dict = {"name": "Alice", "age": 22}
print(my_dict)
# using constructor
mydict2 = dict(name="Bob", age=33)

empty_dict = {}
print(empty_dict)

person = {"name": "Alice", "age": 22}
print(person["name"])
print(person["age"])
person["name"] = "Ahsaan"
print(person["name"])

# Dictionary cannot contain duplicate keys
my_dict3 = {"name": "Bob", "age": 33, "dept": "CSE"}
print(my_dict3["name"])
