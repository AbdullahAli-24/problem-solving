# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 



class Solution:
    def maxProduct( nums):
        nums.sort()
        i=nums[len(nums)-1]
        j=nums[len(nums)-2]
        x=(i-1)*(j-1)
        return print(x)

Solution.maxProduct([3,2,5,1])
Solution.maxProduct([16,47,11,1])
Solution.maxProduct([5,3,8,12])