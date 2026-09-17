class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        #i,
        for i in range(len(nums)):
            max2 = len(nums)-1
            min1 = i+1
            while min1 < max2:
                if (nums[i] ==nums[i-1]) and (i>0):
                    break
                if (max2<len(nums)-1) and (nums[max2] ==nums[max2+1]):
                    max2-=1
                #print(i,j,k)
                elif nums[i]+nums[max2]+nums[min1] <0:
                    min1+=1
                elif nums[i]+nums[max2]+nums[min1] >0:
                    max2-=1
                else:
                    results.append([nums[i],nums[max2],nums[min1]])
                    max2-=1
                    min1+=1
            #i+=1
            #j= len(nums)-1
        return results
                