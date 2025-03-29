from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        slow=2
        fast=2

        while fast<len(nums):
            if nums[fast]!=nums[slow-2]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1

        return slow
    
def test_removeDuplicates():
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = solution.removeDuplicates(nums)
    print(k)
    print(nums)

test_removeDuplicates()



