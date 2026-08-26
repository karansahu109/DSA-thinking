class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0 , len(heights) - 1
        maxVol = 0
        while i < j:
            maxVol = max(maxVol, (j-i)*min(heights[i], heights[j]))
            #If heights[i] is smaller, then any future container using index i will have a smaller width, 
            #and its height is still at most heights[i]
            if heights[i] < heights[j]:
                i +=1
            else:
                j -=1
        return maxVol

        