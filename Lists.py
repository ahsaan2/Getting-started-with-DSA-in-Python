# lists -> a collection of items that are stored in a specific order.
my_list = [1, 2, 3, 4]

# Lists are mutable
my_list[0] = 10
# print(my_list)

my_list = ["i", "am", "in", "a", "list"]
print(my_list)

if len(my_list) > 0:
    print("list is not empty")

# check if 2 is in the list
if 2 in my_list:
    print("2 is in list")
else:
    print("2 is not in list")

    if 4 not in my_list:
        print("4 is not in list")
    else:
        print("we have 4 in the list")

#  looping in lists

for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

#  list functions
my_list = [1, 2, 3, 4]
print("sum is ", sum(my_list))
print("len is ", len(my_list))
print("min is ", min(my_list))
print("max is ", max(my_list))

my_list.append(5)
print("list is now ", my_list)

my_list.pop(0)
print("list after popping numbers: ", my_list)
print(my_list.index(5))

#  list slicing
# list in reverse order
print(my_list[::-1])
print(my_list[1 : 3])
