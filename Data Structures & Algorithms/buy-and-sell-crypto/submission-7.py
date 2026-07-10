class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        if len(prices) <=1:
            return 0
        maxi = max(0,prices[j]-prices[i])
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j
                j+=1
            else:
                if maxi < prices[j]-prices[i]:
                    maxi = prices[j]-prices[i]
                j+=1
        return maxi