# subset is the selection of elements possibly None of the array
from unittest import result


def subsets(nums, index, my_list, result):
    if index == len(nums):
        result.append(my_list[:])
        return
    my_list.append(nums[index])
    subsets(nums, index + 1, my_list, result)
    my_list.pop()
    subsets(nums, index + 1, my_list, result)


nums = [1, 2, 3]
result = []
subsets(nums, 0, [], result)
print(result)
