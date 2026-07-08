def choix(nums):
    if len(nums)%2==0:
        return len(nums)//2
    else:
        return len(nums)//2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = choix(nums)
        j = i
        while len(nums)!=0:
            if nums[i] < target:
                nums = nums[i+1:]
                i = choix(nums)
                j +=i+1
            elif nums[i] > target:
                nums = nums[:i]
                i = choix(nums)
                j -=i+1
            else:
                return j
            print(nums)
        return -1
