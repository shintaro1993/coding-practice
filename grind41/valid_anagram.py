"""Step1

考察：
・ それぞれの文字列に対して，文字の個数をメモする辞書を作り，同じ辞書が出来上がるかどうか調べる．

反省：
・二つの文字列をソートして比較する方法を捨ててしまっていた．

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_to_count = {}

        for c in s:
            if c not in char_to_count:
                char_to_count[c] = 1
                continue
            char_to_count[c] += 1

        for c in t:
            if c not in char_to_count:
                return False
            char_to_count[c] -= 1

        for key, value in char_to_count.items():
            if value != 0:
                return False
        
        return True