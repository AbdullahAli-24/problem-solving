# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


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