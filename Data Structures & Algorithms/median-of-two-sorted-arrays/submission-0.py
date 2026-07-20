class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        for i in range(len(nums2)):
            nums1.append(float('inf'))

        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            
            last -= 1
        

        # spillover of nums2 into nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
            
        length  = len(nums1)
        median = None
        if length % 2 == 0:
            left = length // 2
            right = left + 1
            median = (nums1[left - 1] + nums1[right - 1]) / 2
        else:
            mid = (length + 1) // 2
            median = nums1[mid - 1]
        return median