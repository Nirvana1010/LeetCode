class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = [-1, -1]
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                tmp_left, tmp_right = mid, mid
                while tmp_left >= 0 and nums[tmp_left] == target:
                    tmp_left -= 1
                while tmp_right < n and nums[tmp_right] == target:
                    tmp_right += 1
                result = [tmp_left+1, tmp_right-1]
                return result
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return result