# Pre-storing values into lists or dict or sets
# (1) given n between 1 and 10 and m having 10 to power 8 items
# Find the freq of items in m in the n
from Dictionaries import my_dict

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
my_list = [0] * 11

for i in range(len(n)):
    my_list[n[i]] += 1
print(my_list)

# get the freq of m in n

for num in m:
    if num < 0 or num > 10:
        print("Number is not present!")
    else:
        print("freq of the num in n is ", my_list[num])

# Using dict.

my_dict = {}
for num in n:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
for num in m:
    if num < 0 or num > 10:
        print("Number is not present!")
    else:
        print("key is ", num, "value in dict ", my_dict.get(num))

#  storing string characters in dict
my_dict = {}
name = "ahsaan"
for char in name:
    my_dict[char] = my_dict.get(char, 0) + 1

print(my_dict)
