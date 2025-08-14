def move(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            # print(nums[index])
            index += 1
    for num in nums:
        print(num)
    print(index)
    while index < len(nums):
        nums[index] = 0
        index = index + 1
    print(nums)


nums = [0, 0, 1, 0, 3, 12]
# [1, 3, 12,

print(move(nums))
# print(nums)
