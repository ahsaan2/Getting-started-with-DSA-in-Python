# Generate all the binary sequence of size n

def solve(index, flag, nums, result):
    if index == len(nums):
        result.append("".join(nums))
        # take all the items and concatenate them into a single string when we reach till the end of the string.
        return
    nums[index] = "0"
    solve(index + 1, True, nums, result)
    if flag is True:
        nums[index] = "1"
        solve(index + 1, False, nums, result)
        nums[index] = "0"


def generate(index, flag, nums, result, my_list):
    if index == len(nums):
        result.append("".join(my_list))  # join numbers without any space
        return
    # take 0
    # if False:
    nums[index] = "0"
    my_list.append(nums[index])
    generate(index + 1, True, nums, result, my_list)
    my_list.pop()
    if True:
        nums[index] = "1"
        my_list.append(nums[index])
        generate(index + 1, False, nums, result, my_list)
        my_list.pop()
        nums[index] = "0"


n = 3
nums = [0] * n
my_list = []
result = []
# generate(0, False, nums, result, my_list)
print(result)

solve(0, True, nums, result)
print(result)
# print(nums)
# given an integer, print all the binary strings of size N which do not contain consecutive 1's
# m = 3
# [000, 001, 101, 010, 100
