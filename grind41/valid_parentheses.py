class Solution:
    def isvalid(self, s: str) -> bool:
        parentheses = {')': '(', '}': '{', ']': '['}
        open_brackets = ['(', '{', '[']
        stack = []
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != parentheses[c]:
                    return False
                stack.pop()
        return not stack
            

