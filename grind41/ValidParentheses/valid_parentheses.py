class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close_brackets = ['(': ')', '{': '}', '[': ']']
        stack = []
        for c in s:
            if c in open_to_close_brackets:
                stack.append(c)
                continue
            if not stack or c != open_to_close_brackets[stack[-1]]:
                return False
            stack.pop()
        return not stack