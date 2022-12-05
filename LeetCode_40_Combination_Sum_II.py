class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(candidates, target, combination):
            nonlocal result
            if target == 0:
                result.append(combination[:])
                return
            
            last = -inf
            for i, num in enumerate(candidates):
                if num != last and target - num >= 0:
                    last = num
                    dfs(candidates[i+1:], target - num, combination+[num])
        
        dfs(candidates, target, [])
        return result