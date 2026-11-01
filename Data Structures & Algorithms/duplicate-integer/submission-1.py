class Solution:
    def hasDuplicate(self,nums):
        Seen = set()
        for n in nums:
            if n in Seen:
                return True
            else:
                Seen.add(n)
        return False
