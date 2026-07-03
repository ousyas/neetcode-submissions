class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i] in dict):
                if (dict[target - nums[i]] != i):
                    return[i,dict[target - nums[i]]]



