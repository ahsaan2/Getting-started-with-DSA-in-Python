# given an array find the max sub_array sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# maxi = float('-inf')
# for i in range(len(nums)):
#     sum = 0
#     for j in range(i, len(nums)):
#         sum += nums[j]
#         maxi = max(maxi, sum)
# print(maxi)

maxi = float("-inf")
right = 0
sum = 0
while right < len(nums):
    if sum < 0:
        sum = 0
    sum = sum + nums[right]
    maxi = max(maxi, sum)
    right = right + 1
print(maxi)
