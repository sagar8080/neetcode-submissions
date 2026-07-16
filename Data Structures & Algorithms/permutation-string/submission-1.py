class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base cases
        if len(s1) > len(s2):
            return False
        
        n1, n2 = len(s1), len(s2)
        l, r = 0, n1
        charset = collections.deque()
        target_count = Counter(s1)
        for i in range(n1 - 1, n2):
            curr_str = s2[l:r]
            if Counter(curr_str) == target_count:
                return True
            l += 1
            r += 1
        return False



                

        