class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range (len(nums)):
            difference = target - nums[i]
            if difference in numsMap:
                return [numsMap[difference], i]
            else:
                numsMap[nums[i]] = i
        return None