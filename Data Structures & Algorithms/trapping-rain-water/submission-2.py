class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        MaxL = height[0]
        MaxR = height[len(height)-1]
        while l < r : 
            if MaxL < MaxR:
                l += 1
                MaxL = max(MaxL,height[l])
                res += MaxL - height[l]
            else:
                r -= 1
                MaxR = max(MaxR, height[r])
                res += MaxR - height[r]
      # prefix = 0
        # suffix = 0
        # suffM = [0]*len(height)
        # prefM = [0]*len(height)
        # for i in range(len(height)):
        #     prefM[i] = prefix
        #     prefix = max(prefix,height[i])
        # for i in range(len(height)-1,-1,-1):
        #     suffM[i] = suffix
        #     suffix = max(suffix, height[i])
        # for i in range(len(height)):
        #     if min(prefM[i],suffM[i]) - height[i] < 0:
        #         res += 0
        #     else:
        #         res += min(prefM[i],suffM[i]) - height[i]
       
        return res




        