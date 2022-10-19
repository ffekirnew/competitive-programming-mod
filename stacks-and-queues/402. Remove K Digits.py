class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack or n is not '0':
                stack.append(n)
        while k and stack:
            stack.pop()
            k -= 1
        return ''.join(stack) or '0'
