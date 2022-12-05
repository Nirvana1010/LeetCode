class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        end = 0
        for i in range(n-1):
            max_pos = max(max_pos, nums[i] + i)
            if end == i:
                end = max_pos
        if end < n-1:
            return False
        else:
            return True