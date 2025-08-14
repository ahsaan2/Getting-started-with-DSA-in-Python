# given an array find the max consecutive ones
nums = [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
count = 0
maxi = 0
for num in nums:
    if num == 1:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 0
print(maxi)
