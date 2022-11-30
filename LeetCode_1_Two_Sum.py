class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                j = nums[i+1:].index(diff)
                return [i, j+i+1]