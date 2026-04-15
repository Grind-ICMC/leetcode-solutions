class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_gain = 0
        max_num = 0

        for i in range(N - 2, -1, -1):
            max_num = max(prices[i + 1], max_num)
            max_gain = max(max_gain, max_num - prices[i])

        return max_gain







        