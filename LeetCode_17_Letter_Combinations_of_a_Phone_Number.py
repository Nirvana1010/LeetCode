class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        result = []
        n = len(digits)
        def dfs(path, i):
            if i == n:
                result.append(path)
                return
            letters = digit_letter[digits[i]]
            for c in letters:
                dfs(path+c, i+1)
        
        if not digits:
            return []
        dfs('', 0)
        return result