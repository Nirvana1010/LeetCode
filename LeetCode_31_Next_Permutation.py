class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # search for ascending order between i and i+1
        i = n - 2
        while i > -1:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        
        # search for nums[j] > nums[i]
        if i >= 0:
            j = n - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # [i+1, n] should in ascending order
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return 
    