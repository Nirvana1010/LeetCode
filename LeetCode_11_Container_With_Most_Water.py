class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_val = 0
        while True:
            if left == right:
                break
            if height[left] <= height[right]:
                val = height[left] * (right - left)
                left += 1
            else:
                val = height[right] * (right - left)
                right -= 1
            max_val = max(max_val, val)
        return max_val