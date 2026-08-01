class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 1
        r = length - 2

        while l <= r:
            m = l + (r - l) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m
        # search the left array: 0 to peak
        l = 0
        r = peak - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid

        # search the right subarray: peak to r
        l = peak
        r = length - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val > target:
                l = mid + 1 
            elif val < target:
                r = mid - 1
            else:
                return mid
        
        return -1
        
