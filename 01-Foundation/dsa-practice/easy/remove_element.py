def remove_element(nums, val) -> int:
    # This is the solution i came up with
    # i = 0
    # j = len(nums) - 1
    # while i < j:
    #     print(i, j)
    #     if nums[i] == val and nums[j] != val:
    #         nums[i] = nums[j]
    #         nums[j] = val
    #         i += 1
    #         j -= 1
    #     elif nums[i] == val and nums[j] == val:
    #         j -= 1
    #     else:
    #         i += 1

    # return i

    # This is the better solution
    # So basically in the leetcode site this problem want you to remove element that equal to val from an array without creating new array
    # but the phrasing and that question is really bad, and not even correct explanation
    nums[:] = [x for x in nums if x != val]     # [:] modifiying object without alter their memory address, 
    return len(nums)


print(remove_element([3, 2, 2, 3], 2))