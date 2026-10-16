class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        p = 0
        a = False
        for i in range(len(prices)-1):
            if i==0:
                p = 0
            x = prices[i]
            y = prices[i+1]

            if i == len(prices)-2:
                if y > x:
                    a = True
                    p = p + (y-x)
                    profit = profit+p
            if a :
                if y > x:
                    a = True
                    p = p + (y-x)
                else:
                    profit = profit+p
                    p = 0
            elif y > x:
                a = True
                p = y - x


        return profit