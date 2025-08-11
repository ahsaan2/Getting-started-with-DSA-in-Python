# set is unordered(tuple is ordered)
# Set can contain unique items only
# use of curly-braces
from typing import List

my_set = {1, 2, 3}
print(my_set)

my_set = set()
my_set.add(10)
my_set.add(20)
print(my_set)


# add the numbers in a set

def list_to_set(nums: List[int]) -> set[int]:
    my_set2 = set()
    for i in nums:
        my_set2.add(i)
    return my_set2


print(list_to_set([100, 200, 300]))

# set operations
my_set.remove(10)
print(my_set)

my_set.add(23)
my_set.add(25)

for num in my_set:
    print(num)

#     converting list to the set
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set = set(my_list)
print("updated set is ", my_set)

print("cat" in my_set)
print(6 in my_set)
nums = {1, 2, 3, 4}


