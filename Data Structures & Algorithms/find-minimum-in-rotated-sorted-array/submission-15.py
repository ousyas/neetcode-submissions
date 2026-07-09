class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = -1
        k = i
        while -j<=len(nums)//2+1:
            if nums[k] <=nums[k-1]:
                return nums[k]
            elif (nums[k] >= nums[k-1]) and (nums[k] > nums[k+1]):
                return nums[k+1]
            else:
                if k>=0:
                    k = j
                    i+=2
                else:
                    k = i
                    j-=1



            