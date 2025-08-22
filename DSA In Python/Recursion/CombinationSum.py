# Given an array of distinct nums and a target , return all the unique combinations where the sum is equal to the
# target. The same number may be chosen a number of times


def combinations(index, nums, target, my_list, result):
    if index == len(nums):
        if target == 0:
            result.append(my_list[:])
            return
        return
    if nums[index] <= target:
        my_list.append(nums[index])
        combinations(index, nums, target - nums[index], my_list, result)
        # backtrack
        my_list.pop()
    combinations(index + 1, nums, target, my_list, result)

nums = 2, 3, 6, 7
target = 7
result = []
combinations(0, nums, target, [], result)
print(result)