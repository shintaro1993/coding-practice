"""Step1

11行目のjの値をi+1にしていないことによるエラー

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit