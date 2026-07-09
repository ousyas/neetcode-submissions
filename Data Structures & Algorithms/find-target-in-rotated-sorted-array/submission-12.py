class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)
        while right - left >2:
            mid = (right+left)//2
            if nums[left]<nums[mid]:
                if (target >= nums[left]) and(target < nums[mid]):
                    right = mid+1
                    mid = (right+left)//2
                elif target == nums[mid]:
                    return mid
                else:
                    left = mid
                    mid = (right+left)//2
            else:
                if (target > nums[mid]) and (target < nums[left]):
                    left = mid
                    mid = (right+left)//2
                elif target == nums[mid]:
                    return mid
                else:
                    right = mid+1
                    mid = (right+left)//2
            print(nums[left:right])
        if (nums[left] == target):
            return left
        elif (nums[right -1] == target):
            return right-1
        else:
            return-1