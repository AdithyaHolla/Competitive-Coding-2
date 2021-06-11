"""
Time Complexity : O(n^2)
Space Complexity : O(1)
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1,-1]
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                
                if target == nums[i] + nums[j]:
                    return [i,j]
        
        return [-1,-1]
        