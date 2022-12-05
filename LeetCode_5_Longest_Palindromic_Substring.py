class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandPalindromic(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        
        n = len(s)
        max_len = 0
        result = ''
        for i in range(n):
            left, right = expandPalindromic(i, i)
            if right - left + 1 > max_len:
                result = s[left : right + 1]
                max_len = right - left + 1
            
            left, right = expandPalindromic(i, i+1)
            if right - left + 1 > max_len:
                result = s[left : right + 1]
                max_len = right - left + 1
        return result