class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            tmp = abs(nums[i])
            if tmp <= n:
                nums[tmp - 1] = -abs(nums[tmp - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
    
    