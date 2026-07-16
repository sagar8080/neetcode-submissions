class Solution:
    def tribonacci(self, n: int) -> int:
        T0, T1, T2 = 0, 1, 1
        if n == 0:
            return T0
        elif n == 1:
            return T1
        elif n == 2:
            return T2
        curr_num = T0 + T1 + T2
        for i in range(3, n+1):
            curr_num = T0 + T1 + T2
            T0, T1, T2 = T1, T2, curr_num
        
        return curr_num