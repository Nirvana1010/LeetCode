class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        def mergeSort(nums, l, r):
            if l == r:
                return
            mid = (l + r) // 2
            mergeSort(nums, l, mid)
            mergeSort(nums, mid+1, r)
            
            tmp = []
            i, j = l, mid + 1
            while i <= mid or j <= r:
                if i > mid or (j <= r and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[l : r+1] = tmp
        
        def partition(nums, l, r):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l - 1
            for j in range(l, r):
                if nums[j] < nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        def quickSort(nums, l, r):
            if r <= l:
                return
            mid = partition(nums, l, r)
            quickSort(nums, l, mid - 1)
            quickSort(nums, mid + 1, r)
            
        quickSort(nums, 0, n-1)
        return
    
    