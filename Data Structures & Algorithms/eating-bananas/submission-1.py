class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Return the minimum k such that you can eat all the bananas within h hours
    
        n = len(piles)
        l = 1
        r = max(piles)
        res = r

        
        while l<=r:
            k = (l + r)//2
            hPile = 0
            for pile in piles :
                hPile += math.ceil(pile/k)
            if hPile<=h :
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        return res






        