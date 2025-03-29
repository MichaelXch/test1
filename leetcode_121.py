from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0

        for price in prices:
            if minprice>price :
                minprice=price
            elif price-minprice>maxprofit:
                maxprofit=price-minprice
        return maxprofit
            
def test_maxProfit():
    solution = Solution()
    
    # 测试用例1: 价格波动
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"
    
    # 测试用例2: 价格持续上涨
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4, "Test case 2 failed"
    
    # 测试用例3: 价格持续下跌
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, "Test case 3 failed"
    
    # 测试用例4: 空列表
    assert solution.maxProfit([]) == 0, "Test case 4 failed"
    
    # 测试用例5: 只有一个价格
    assert solution.maxProfit([5]) == 0, "Test case 5 failed"
    
    print("All test cases passed!")

test_maxProfit()