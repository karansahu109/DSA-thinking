class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        if len(s) != len(t):
            return False
        # numTable = {}
        # for i in range (len(s)):
        #     if s[i] not in numTable:
        #         numTable[s[i]] = 1
        #     else:
        #         numTable[s[i]] += 1
        # for i in range (len(t)):
        #     if t[i] not in numTable:
        #         return False
        #     else:
        #         numTable[t[i]] -= 1
            
        #     if numTable[t[i]] < 0:
        #         return False
        # return True
        for c1,c2 in zip(s,t):
            freq[ord(c1)-ord("a")] += 1
            freq[ord(c2)-ord("a")] -= 1
        for n in freq:
            if n != 0: 
                return False
        return True

        