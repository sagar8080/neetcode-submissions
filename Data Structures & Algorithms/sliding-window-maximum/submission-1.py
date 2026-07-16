class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []
        l, r = 0, k
        window = collections.deque(nums[l : r])
        max_num = max(window)
        res = []
        res.append(max_num)
        for i in range(k, n):
            # if nums[i] > max_num:
            #     max_num = nums[i]
            window.popleft()
            window.append(nums[i])
            max_num = max(window)
            res.append(max_num)
        
        return res
        