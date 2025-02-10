"""Step2

考察：
・ それぞれの文字列に対して，文字の個数をメモする辞書を作り，同じ辞書が出来上がるかどうか調べる．

反省：
・二つの文字列をソートして比較する方法を捨ててしまっていた．

"""

class Solution:
    def make_letter_to_count_dict(s):
        letter_to_count = {}
        for c in s:
            if c not in letter_to_count:
                letter_to_count[c] = 1
                continue
            letter_to_count[c] += 1
        return letter_to_count

    def isAnagram(self, s: str, t: str) -> bool:
        return make_letter_to_count(s) == make_letter_to_count(t)


