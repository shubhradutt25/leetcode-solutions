class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum_price = prices[0]
        maximum_profit=0
        for price in prices:
            if price < minimum_price:
                minimum_price = price 
            else:
                profit=price-  minimum_price
                if profit> maximum_profit:
                    maximum_profit= profit
        return maximum_profit
        