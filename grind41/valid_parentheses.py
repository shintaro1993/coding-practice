""" Step2

異常な値が入ってきたときにどうするか考える癖をつける

"""

class Solution:
    def isValid(self, s:str) -> bool:
        open_to_close_of_same_prarentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in open_to_close_of_same_parentheses:
                stack.append(c)
                continue
            if not stack:
                return False
            if c != open_to_close_of_same_parentheses[stack[-1]]:
                return False
            stack.pop()
        return not stack

            
