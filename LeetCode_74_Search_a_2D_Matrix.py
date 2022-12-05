class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m-1
        column_0 = [row[0] for row in matrix]
        column_0.append(column_0[-1] + 1)
        target_row = []
        while left <= right:
            mid = (left + right) // 2
            if column_0[mid] <= target < column_0[mid + 1]:
                target_row = matrix[mid]
                break
            if column_0[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        target_row = matrix[mid]
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if target_row[mid] == target:
                return True
            if target_row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False