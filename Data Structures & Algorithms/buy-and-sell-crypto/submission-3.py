class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        profit = 0
        lowest_seen_price = prices.pop(0)
        for current_day in range(len(prices)):
            cur_price = prices[current_day]
            profit = cur_price - lowest_seen_price
            #print(f"i {current_day}, cp {cur_price}, prof {profit}, lp {lowest_seen_price}")
            if cur_price < lowest_seen_price:
                lowest_seen_price = cur_price
            if profit > best_profit:
                best_profit = profit

        
        
        
        return best_profit
