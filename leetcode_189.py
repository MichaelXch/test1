from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newnums= [0]*len(nums)
        length = len(nums)
        for i in range(length):
            j=(i+k) % length
            newnums[j]=nums[i]
        nums[:] = newnums


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        def reversed(arr:list[int],start:int,end:int)->None:
            while start<end:
                arr[start],arr[end] = arr[end],arr[start]
                start+=1
                end-=1
        
        reversed(nums,0,n-1)
        reversed(nums,0,k-1)
        reversed(nums,k,n-1)

def test_rotate():
    solution = Solution1()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    print(nums)

test_rotate()
