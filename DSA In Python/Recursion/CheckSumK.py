# Part A
# Generate all subseq with the sum = k

def find(index, nums, target, my_list, my_list1):
    if index == len(nums):
        # if sum(my_list) == target:
        if target == 0:
            my_list1.append(my_list[:])
            return
        else:
            return
            # we can take the index value only if it is less than the target
    if nums[index] <= target:
        my_list.append(nums[index])
        find(index + 1, nums, target - nums[index], my_list, my_list1)
        my_list.pop()
    find(index + 1, nums, target, my_list, my_list1)


nums = [10, 1, 2, 7, 6, 1, 5]
k = 8
my_list1 = []
find(0, nums, k, [], my_list1)
print(my_list1)


# Part B
# Given nums and a target sum k, check whether there exists a subsequence such that
# the sum of all elements in the subseq equals target

def check(index, nums, target, my_list, my_list1) -> bool:
    if index == len(nums):
        if target == 0:
            my_list1.append(my_list[:])
            return True
        else:
            return False
    pick = False
    if nums[index] <= target:
        my_list.append(nums[index])
        pick = check(index + 1, nums, target - nums[index], my_list, my_list1)
        my_list.pop()
    notpick = check(index + 1, nums, target, my_list, my_list1)
    return pick or notpick


nums = [10, 1, 2, 7, 6, 1, 5]
k = 8
my_list1 = []
my_list = []
print(check(0, nums, k, my_list, my_list1))
# print(my_list1)
