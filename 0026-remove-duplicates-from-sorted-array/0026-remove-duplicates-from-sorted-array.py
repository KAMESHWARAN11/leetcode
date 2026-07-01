class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        for i in nums:
            if i != nums[k]:
                nums[k+1] = i 
                k += 1
        return k+1
            