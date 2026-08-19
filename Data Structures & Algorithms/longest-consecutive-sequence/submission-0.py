class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seq = 0
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                seq = 1
                while (num + seq) in numSet:
                    seq += 1 
                    longest = max(seq, longest)
           
        return max(longest , seq)
            


        