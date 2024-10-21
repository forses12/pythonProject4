def two_sum(nums, target):
    for num in range(len(nums)):
        for n in range(num+1,len(nums)):
            if nums[num]+nums[n]==target: return [num,n]
print(two_sum([3,3],6))
print(2*(10**(len(str(1812))-1)))