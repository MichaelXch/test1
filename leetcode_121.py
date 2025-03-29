from typing import List


class Solution:
        
    def maxProfit(self, prices: List[int]) -> int:
        """
        计算可获得的最大利润。
        
        Args:
            prices: 股票每天的价格列表
            
        Returns:
            可获得的最大利润
        """
        minprice=float('inf')
        maxprofit=0
        
        for price in prices:
            if minprice>price :
                minprice=price
            elif price-minprice>maxprofit:
                maxprofit=price-minprice
        return maxprofit
            
def test_maxProfit():
    """
    测试maxProfit函数的各种情况。
    
    测试用例包括:
    1. 价格波动的情况 - 验证函数能否找到最佳买卖点
    2. 价格持续上涨的情况 - 验证函数能否处理单调递增序列
    3. 价格持续下跌的情况 - 验证函数能否正确返回0
    4. 空列表的情况 - 验证函数对边界情况的处理
    5. 只有一个价格的情况 - 验证函数对最小输入的处理
    
    无返回值，如果所有测试用例通过则打印成功信息，否则抛出AssertionError。
    """
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