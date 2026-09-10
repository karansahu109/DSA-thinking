class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
           
        for n,c in count.items():
            freq[c].append(n) 
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

            