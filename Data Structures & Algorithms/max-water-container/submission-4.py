class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1

        resultats = [min(heights[i],heights[j])*(j-i)]
        while i<j:
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            resultats.append(min(heights[i],heights[j])*(j-i))
        return max(resultats)
            