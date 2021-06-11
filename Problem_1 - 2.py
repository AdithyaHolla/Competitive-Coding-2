"""
Time Complexity : O(n)
Space Complexity : O(n)
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1,-1]
        
        hashmap = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            else:           
                hashmap[nums[i]] = i
        
        return [-1,-1]
        
       