class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0 , len(heights) - 1
        maxVol = 0
        while i < j and i != j:
            maxH = min(heights[i],heights[j])
            currVol = maxH*(j-i)
            maxVol = max(maxVol,currVol)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxVol
