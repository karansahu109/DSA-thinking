class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numTableS = {}
        numTableT = {}
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            numTableS[s[i]] = numTableS.get(s[i],0) + 1
            numTableT[t[i]] = numTableT.get(t[i],0) + 1
           

        if numTableS == numTableT:
            return True
        return False

        