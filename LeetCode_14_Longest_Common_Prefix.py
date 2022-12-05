class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for string in strs:
            n = min(len(result), len(string))
            tmp_str = string[:n]
            result = result[:n]
            while result and tmp_str != result:
                result = result[:-1]
                tmp_str = tmp_str[:-1]
            if not result:
                return ''
        return result