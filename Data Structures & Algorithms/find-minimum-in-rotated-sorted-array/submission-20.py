class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]        
        else:
            while len(nums)>=3:
                if nums[len(nums)//2]>=nums[0]:
                    nums = nums[len(nums)//2:]
                    print(nums,len(nums)//2)
                else:
                    nums = nums[:len(nums)//2+1]
                    print(nums)
        return min(nums)
                






            