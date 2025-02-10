"""Step1

 反省：
 ・visitedの追加処理を忘れている．
 ・imageにimageを代入してしまっている．
 ・範囲チェックのm, nを間違えている

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

