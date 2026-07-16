class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum, s)).strip().lower()
        n = len(string) - 1
        for i in range(n):
            left_char = string[i]
            right_char = string[n-i]
            if left_char != right_char:
                return False
        return True

        