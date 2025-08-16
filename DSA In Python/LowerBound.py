arr =  [2, 3, 7, 10, 11, 11, 25]
target = 9
# The lower bound of a number is defined as the smallest index in the sorted array
# where the element is greater than or equal to the given number.
# Here, we can see the smallest number that is greater than the target is 10 (index 3)

start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end) // 2
    # if arr[mid] == target:
    #     print(mid)
    #     break
    if arr[mid] >= target:
        end = mid - 1
    else:
        start = mid + 1
print(start)
