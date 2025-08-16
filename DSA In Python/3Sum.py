nums = [-1, 0, 1, 2, -1, -4]
# return all triplets such that the indexes of the 3 don't match
# triplet sum should be 0
# [-4, -1, -1, 0, 1, 2]
# [-1, -1, 2]  sum = 0
# [-1, 0, 1]
# case 1 , when the sum < 0, we have to move towards right
# case 2, when the sum > 0, we have to move towards left
# case 3, when the sum == 0, we add the triplets
my_list = []
my_set = set()
# [-4, -1, -1, 0, 1, 2]
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        i += 1
    j = i + 1
    k = len(nums) - 1
    while j < k:
        # take the sum
        item_sum = nums[i] + nums[j] + nums[k]
        if item_sum < 0:
            j += 1
        elif item_sum > 0:
            k -= 1
        else:
            # we have the sum = 0
            print("total sum is  ",item_sum)
            # my_list.append([nums[i], nums[j], nums[k]])
            my_set.add(tuple([nums[i], nums[j], nums[k]]))
            k -= 1
            j -=1
# iterate over the set to add them in the list
my_list = [list(t) for t in my_set]
print(my_list)