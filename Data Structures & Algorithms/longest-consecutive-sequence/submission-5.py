class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxSeq = 0
        for n in nums:
            if n-1 not in mySet:
                cur = n
                length = 1
                while cur + 1  in mySet: 
                    length += 1
                    cur += 1 
                maxSeq = max(maxSeq,length)
        return maxSeq
        

            


        