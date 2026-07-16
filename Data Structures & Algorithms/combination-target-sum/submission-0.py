class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # define a global array to store res
        res = []

        # define the dfs function
        def dfs(i, cur, total):
            # base case: total > target
            if total > target or i >= len(nums):
                return
            
            # base case: total = target
            if total == target:
                res.append(cur.copy())
                return

            # 2 branch decision
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        # call the dfs function
        dfs(0, [], 0)
        # return res
        return res
        