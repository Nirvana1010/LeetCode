class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        max_len = 0
        while right < n:
            while s[right] in s[left : right]:
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len