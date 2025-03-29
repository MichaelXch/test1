from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
    
def test_maxProfit():
    solution = Solution()
    
    # 测试用例1: 价格波动，多次买卖
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7, "Test case 1 failed"
    
    # 测试用例2: 价格持续上涨，多次买卖
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4, "Test case 2 failed"
    
    # 测试用例3: 价格持续下跌，不买卖
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, "Test case 3 failed"
    
    # 测试用例4: 空列表
    assert solution.maxProfit([]) == 0, "Test case 4 failed"
    
    # 测试用例5: 只有一个价格
    assert solution.maxProfit([5]) == 0, "Test case 5 failed"
    
    # 测试用例6: 价格波动，多次买卖
    assert solution.maxProfit([1, 5, 3, 6, 4, 7]) == 10, "Test case 6 failed"
    
    print("All test cases passed!")

test_maxProfit()