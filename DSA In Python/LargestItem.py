nums = [55, 32, 97, 99, 3, 67]

largest = nums[0]
for num in nums:
    largest = max(largest, num)
    # if num > largest:
    #     largest = num

print("largest:", largest)

nums = [12, 21, 23, 21, 23, 434, 232]
print("max number is ", max(nums))

# Find the second-largest items in the nums array
nums = [12, 21, 23, 21, 23, 434, 232, 500, ]
largest = nums[0]
prev_largest = 0
for num in nums:
    if num > largest:
        prev_largest = largest
        largest = num
    if prev_largest < num < largest:
        # if prev_largest < num and num < largest:
        prev_largest = num

print("Second largest is ", prev_largest, "largest is ", largest)
