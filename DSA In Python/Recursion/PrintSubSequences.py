# print all the subsequences
# "continuous" or "non-continuous" sequence which follows a specific order
# Each time we have the option of either take an item or not.
# We cannot pick any of the items
# [9, 5, 7] -> [9], [5], [7], [9, 5],[9, 7],[9, 5, 7], [5, 7], []
# def findSequence(param, my_list, my_lit1, nums):
#     pass


def findSequence(index, my_list, my_list1, nums):
    if index == len(nums):
        my_list1.append(my_list[:]) # takes a snapshot of the current list we have, and makes a shallow copy
        return
    # take / add and move
    my_list.append(nums[index])
    findSequence(index + 1, my_list, my_list1, nums)
    # my_list1.remove(len(my_list) - 1)
    my_list.pop()
    findSequence(index + 1, my_list, my_list1, nums)


nums = [1, 2, 3]
# my_list = []
my_list1 = []
findSequence(0, [], my_list1, nums)
print(my_list1)
