# Rotate the array by k steps
from typing import List

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# we can remove the last k numbers and append them in the front
# while k > 0:
#     val = nums.pop(len(nums) - 1)
#     nums.insert(0, val)
#     print(nums[0])
#
#     k = k - 1
# print(nums)
# Solution 2
# We have store the k items in the temp array and then move the remaining items to the end, and add the temp items at the first
temp = []
for i in range(len(nums) - k, len(nums)):
    temp.append(nums[i])

# print(temp)

# now move remaining items to the end
for i in range(len(nums) - 1, k - 1, -1):
    nums[i] = nums[i - k]
# print(nums)

for i in range(len(temp)):
    nums[i] = temp[i]
print(nums)


# using the reverse function

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
    print("reversed nums ", nums)


def reverse(nums: List[int], start: int, end: int) -> None:
    while start < end:
        temp1 = nums[start]
        nums[start] = nums[end]
        nums[end] = temp1
        start += 1
        end -= 1


num = [1, 2, 3, 4, 5, 6, 7]
k = 3
