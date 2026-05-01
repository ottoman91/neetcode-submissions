# create a variable called max_profit. initialie it to zero. 
# 2. have two pointers, left and right, initilize at zero and 1 
# 3. while right < len(nums) 
# 4. if prices[right] < prices[left]: then move left to right. 
# 5. else calculate max(max_profit, prices[right] - prices[left])
# and increment right by 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_profit = 0 
        left, right = 0, 1 
        while right < len(prices): 
            if prices[right] < prices[left]:
                left = right 
            else:
                max_profit = max(max_profit, prices[right] - prices[left])  
            right+= 1
        return max_profit
