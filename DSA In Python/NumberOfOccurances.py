arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
count = 0
start = 0
end = len(arr) -1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] > target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1
    else:
        index = mid
        count = count + 1
        while index > start and arr[index - 1] == target:
            index = index - 1
            count = count + 1
        # my_list[0] = index
        index = mid + 1
        if arr[index] == target:
            count = count + 1
        while index < end and arr[index + 1] == target:
            index = index + 1
            count = count + 1
        # my_list[1] = index
        break
print(count)