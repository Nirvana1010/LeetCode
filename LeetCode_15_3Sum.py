class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        target = 0
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[n-1] + nums[n-2] < target:
                continue
            if nums[i] + nums[i+1] + nums[i+2] > target:
                break
            left, right = i+1, n-1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif tot < target:
                    left += 1
                elif tot > target:
                    right -= 1

        return result