class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(nums, path):
            if len(path) == n:
                result.append(path[:])
                return
            for i, num in enumerate(nums):
                dfs(nums[:i] + nums[i+1:], path + [num])
        
        dfs(nums, [])
        return result