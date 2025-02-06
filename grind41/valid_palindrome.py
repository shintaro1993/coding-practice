""" Step2

どうして以下のコードを書いてしまったのか考える

・ひとつのステップですべてを終わらせようとしすぎていた．
・rightの初期化を間違えている
・上記含めて場合分けが整理できていない（どの段階で何を保証したいのかをシンプルに整理するようにする）

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left >= right or s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True