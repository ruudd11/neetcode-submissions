class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        top = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                j += 1
                
            else:
                j = 0
            
            top = max(top, j)
        return top
            