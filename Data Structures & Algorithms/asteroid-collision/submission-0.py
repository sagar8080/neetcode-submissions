class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                if diff > 0: # -4 5
                    a = 0
                elif diff < 0: # -4 3
                    stack.pop()
                else: # -4 4
                    a = 0
                    stack.pop()

            if a:
                print(f"Appending {a} to stack")
                stack.append(a)
        return stack