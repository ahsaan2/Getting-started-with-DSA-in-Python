nums = [-1, 0, 3, 5, 9, 12]
target = 9

start = 0
end = len(nums) - 1
while start <= end:
    mid = (start + end) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

