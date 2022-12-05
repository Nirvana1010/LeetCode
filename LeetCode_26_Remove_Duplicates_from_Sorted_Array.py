class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        prev = nums[0]
        while i < n:
            if nums[i] == prev:
                nums.remove(nums[i])
                nums.append('_')
            elif nums[i] == '_':
                break
            elif nums[i] > prev:
                prev = nums[i]
                i += 1

        return i