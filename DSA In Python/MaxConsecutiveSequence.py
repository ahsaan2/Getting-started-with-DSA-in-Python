nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

my_set = set(nums)
# check for the first item
maxi = 0
for num in nums:
    if num - 1 not in my_set:
        current = num
        count = 1
        while current + 1 in my_set:
            count += 1
            current = current + 1
            maxi = max(maxi, count)
print(maxi)
