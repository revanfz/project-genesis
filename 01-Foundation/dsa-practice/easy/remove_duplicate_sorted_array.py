def remove_duplicate(nums):
    num_set = set()
    i = 0
    while i < len(nums):
        if nums[i] in num_set:
            nums.pop(i)
        else:
            num_set.add(nums[i])
            i += 1

    return len(num_set)


print(remove_duplicate([1, 1, 2]))
