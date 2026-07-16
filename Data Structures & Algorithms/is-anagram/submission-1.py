class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s, t = sorted(s), sorted(t)
            if s != t:
                return False
            return True
        