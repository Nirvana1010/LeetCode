class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key=lambda x: x[0])
        l, r = 0, 0
        for item in intervals:
            if not stack or item[0] > stack[-1][1]:
                stack.append(item)
                l, r = stack[-1][0], stack[-1][1]
            else:
                new_interval = item
                while stack and (l <= new_interval[0] <= r):
                    last_interval = stack.pop()
                    if stack:
                        l, r = stack[-1][0], stack[-1][1]
                    new_interval = [min(last_interval[0], new_interval[0]), max(last_interval[1], new_interval[1])]
                stack.append(new_interval)
                l, r = stack[-1][0], stack[-1][1]
        return stack