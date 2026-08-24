from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(min_price, price)

        return max_profit
