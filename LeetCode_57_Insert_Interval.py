class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(0, [-inf, -inf])
        intervals.append([inf, inf])
        
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] < intervals[i+1][0]:
                intervals.insert(i+1, newInterval)
                break
                
        intervals.pop()
        intervals.pop(0)
        
        stack = []
        for item in intervals:
            if not stack or (item[0] > stack[-1][1]):
                stack.append(item)
            else:
                new_inter = item
                while stack and new_inter[0] <= stack[-1][1]:
                    last_inter = stack.pop()
                    new_inter = [min(last_inter[0], new_inter[0]), max(last_inter[1], new_inter[1])]
                stack.append(new_inter)
        return stack