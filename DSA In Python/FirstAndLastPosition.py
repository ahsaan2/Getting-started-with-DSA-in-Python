# nums = [5,7,7,8,8,10]
nums = [5,7,7,8,8,10]
target = 8
# given an array of integers nums sorted in non-decreasing order, find the starting and
# ending position of the given target value

#  5 7 7 8 8 10
my_list = [-1, -1]
start = 0
end = len(nums) - 1
while start <= end:
    mid = (start + end) // 2
    if nums[mid] > target:
        end = mid - 1
    elif nums[mid] < target:
        start = mid + 1
    else:
        # we have the target
        index = mid
        # go to the left
        while index > start and nums[index - 1] == target:
            index = index - 1
        my_list[0] = index
        index = mid
        while index < end and nums[index + 1] == target:
            index = index + 1
        my_list[1] = index

        break
print(my_list)
