class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]        
        else:
            left = 0
            right = len(nums)
            while (right - left) >2:
                print(left,right)
                if nums[(right+left)//2]>=nums[left]:
                    left = (right+left)//2
                    print(left)
                else:
                    right = (right+left)//2 +1
                    print(right)
            print(left,right)
        return min(nums[left:right])
                






            