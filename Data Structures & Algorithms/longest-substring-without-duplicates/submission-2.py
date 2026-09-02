class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        uniSet = set()
        lenSub = 0

        for r in range(len(s)):
            while s[r] in uniSet:
                uniSet.remove(s[l])
                l += 1

            uniSet.add(s[r])
            lenSub = max(lenSub, r - l + 1)

        return lenSub