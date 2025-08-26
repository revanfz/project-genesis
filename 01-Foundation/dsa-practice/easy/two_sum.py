def two_sum(nums, target):
    # O(n^2)
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
            
    #O(n)
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
            
nums = input("Masukkan angka (pisahkan dengan spasi): ").split()
target = input("Masukkan target: ")
print(two_sum([int(s) for s in nums], int(target)))