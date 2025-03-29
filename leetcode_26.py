from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        map={}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=1
                nums[k]=nums[i]
                k+=1
            else:
                i+=1

        return k
    
def test_removeDuplicates():
    solution = Solution()
    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    print(k)
    print(nums)

test_removeDuplicates()
