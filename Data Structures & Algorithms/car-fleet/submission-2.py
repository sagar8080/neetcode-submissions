class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        for i in range(n):
            position, speed = pairs[i]
            t = (target - position) / speed

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)