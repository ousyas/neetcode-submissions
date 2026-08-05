class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        i,j = 0,len(nums)-1
        while i<j:
            k = i+1
            while k < j:
                #print(i,j,k)
                if nums[i]+nums[j]+nums[k] <0:
                    k+=1
                elif nums[i]+nums[j]+nums[k] >0:
                    j-=1
                else:
                    results.append([nums[i],nums[j],nums[k]])
                    j-=1
                    k+=1
            i+=1
            j= len(nums)-1
        print(nums)
        dic = {}
        for result in results:
            if tuple(result) in dic.keys():
                continue
            else:
                dic[tuple(result)] = 1
        return list(dic.keys())
                