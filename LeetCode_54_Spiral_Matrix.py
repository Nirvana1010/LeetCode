class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        def peel(left, right, top, bottom):
            nonlocal result
            if left > right-1 or top > bottom-1:
                return
            
            for j in range(left, right):
                result.append(matrix[top][j])
            for i in range(top+1, bottom):
                result.append(matrix[i][right-1])
            if left < right - 1 and top < bottom - 1:
                for j in range(right-2, left-1, -1):
                    result.append(matrix[bottom-1][j])
                for i in range(bottom-2, top, -1):
                    result.append(matrix[i][left])
            peel(left+1, right-1, top+1, bottom-1)
        m, n = len(matrix), len(matrix[0])
        peel(0, n, 0, m)
        return result