"""Step1

11�s�ڂ�j�̒l��i+1�ɂ��Ă��Ȃ����Ƃɂ��G���[

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit