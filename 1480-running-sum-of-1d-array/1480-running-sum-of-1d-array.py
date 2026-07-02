class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        prefix = 0 
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            a.append(prefix)
        return a