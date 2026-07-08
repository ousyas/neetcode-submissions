class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)//2
        j = i
        while len(nums)!=0:
            if nums[i] < target:
                nums = nums[i+1:]
                i = len(nums)//2
                j +=i+1
            elif nums[i] > target:
                nums = nums[:i]
                i = len(nums)//2
                j -=i+1
            else:
                return j
            print(nums)
        return -1
