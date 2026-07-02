class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        prefix = 0 
        for i in nums:
            prefix += i
            a.append(prefix)
        return a