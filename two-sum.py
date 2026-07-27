class Solution:
    def twoSum(nums, target):
       
        for x in range(len(nums)):
            
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    return print([x,y])


Solution.twoSum([2,7,6,2],9)
Solution.twoSum([2,7,6,2],8)
Solution.twoSum([5,7,4,2],9)
Solution.twoSum([3,7,6,2],13)