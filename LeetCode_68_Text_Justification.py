class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        str_num, line = 0, []
        for word in words:
            if str_num + len(line) - 1 + len(word) >= maxWidth:
                remain = maxWidth - str_num
                for i in range(remain):
                    line[i % max((len(line) - 1), 1)] += ' '
                result.append(''.join(line))
                line = []
                str_num = 0
            line.append(word)
            str_num += len(word)
        result += [' '.join(line).ljust(maxWidth)]
        return result