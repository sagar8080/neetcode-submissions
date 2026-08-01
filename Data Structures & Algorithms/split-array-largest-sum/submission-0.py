class Solution:
    def get_prefix(self, arr):
        n = len(arr)
        prefix_arr = [0] * (n + 1)
        for i in range(n):
            prefix_arr[i + 1] = prefix_arr[i] + arr[i]
        return prefix_arr
    
    def feasible(self, arr, largest, k):
        subarrays = 0
        i = 0
        n = len(arr) - 1
        while i < n:
            l, r = i+1, n

            while l <= r:
                mid = l + (r - l) // 2
                
                if arr[mid] - arr[i] <= largest:
                    l = mid + 1
                else:
                    r = mid - 1
            
            subarrays += 1
            i = r

            if subarrays > k:
                return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        prefix = self.get_prefix(nums)
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            if self.feasible(prefix, mid, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
