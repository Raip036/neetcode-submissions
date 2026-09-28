class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        best = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left= right

            else:
                profit = prices[right] - prices[left]
                best = max(best, profit)
                right += 1

        return best