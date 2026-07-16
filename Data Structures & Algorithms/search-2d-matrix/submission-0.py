class Solution:
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l - 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_values = [i[0] for i in matrix]
        row = self.search(row_values, target)
        search_space = matrix[row]
        result = search_space[self.search(search_space, target)]
        if result == target:
            return True
        return False
        