import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        length=len(nums)
        for i in range(length):
            if nums[i] not in map:
                map[nums[i]]=1
            else:
                map[nums[i]]+=1
            
            if map[nums[i]]>int(length/2):
                return nums[i]
            



class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)  # 统计每个元素的出现次数
        return max(counts.keys(), key=counts.get)  # 返回出现次数最多的元素
    
def test_majorityElement():
    solution = Solution1()
    nums = [2,2,1,1,1,2,2]
    result = solution.majorityElement(nums)
    print(result)

test_majorityElement()
