class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidates, path, sum_result):
            if sum_result == target:
                result.append(path[:])
                return
            for i, num in enumerate(candidates):
                if sum_result < target:
                    dfs(candidates[i:], path+[num], sum_result+num)
        
        dfs(candidates, [], 0)
        return result