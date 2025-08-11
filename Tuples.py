# tuples is an "immutable"-ordered collection of elements, Once created, we cannot change, add, remove items
from typing import Tuple

# using parenthesis
my_tuple = (1, 2, 3, 4)
print("tuple using parenthesis ", my_tuple)
# without parenthesis
my_tuple2 = 1, 2, 3, 4, 5
print("tuple without parenthesis ", my_tuple2)
print("sliced tuple", my_tuple2[1:])
print("tuple sum is ", sum(my_tuple2))

# Single element tuple, must have a comma
single_element = (1,)


# Tuple's allow duplicates, and can contain mixed data types

def create_pair(name: str, age: int) -> Tuple[str, int]:
    return name, age


print(create_pair("John", 22))
