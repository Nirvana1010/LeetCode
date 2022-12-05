class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = {}
        for string in strs:
            anagram = list(string)
            anagram.sort()
            anagram = ''.join(anagram)
            if anagram in word_hash:
                word_hash[anagram].append(string)
            else:
                word_hash[anagram] = [string]
        result = list(word_hash.values())
        print(word_hash)
        return result