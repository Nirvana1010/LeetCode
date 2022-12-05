class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        def dfs(nums, path):
            nonlocal result
            if len(nums) == 0:
                if path not in result:
                    result.append(path[:])
                return
            last = -11
            for i, num in enumerate(nums):
                if num != last:
                    last = num
                    dfs(nums[:i] + nums[i+1:], path + [num])
            
        dfs(nums, [])
        return result