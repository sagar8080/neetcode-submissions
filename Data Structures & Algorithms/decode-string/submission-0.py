class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                substring = ""
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                if stack:
                    stack.pop()
                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                
                stack.append(int(times) * substring)
        
        return "".join(stack)

