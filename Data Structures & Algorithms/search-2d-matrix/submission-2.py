def search( nums: List[int], target: int) -> int:
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
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix)//2
        while len(matrix) > 1:
            print(matrix[0])
            if matrix[i][0] < target:
                matrix = matrix[i:]
                print(matrix)
                i = len(matrix)//2
            elif matrix[i][0] > target:
                matrix = matrix[:i]
                print(matrix)
                i = len(matrix)//2
            else:
                return True
        if len(matrix) ==1:
            return search(matrix[0],target)
        else:
            return False
        