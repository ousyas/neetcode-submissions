class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1

        resultat = min(heights[i],heights[j])*(j-i)
        while i<j:
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            if resultat < min(heights[i],heights[j])*(j-i):
                resultat =  min(heights[i],heights[j])*(j-i)
        return resultat
            