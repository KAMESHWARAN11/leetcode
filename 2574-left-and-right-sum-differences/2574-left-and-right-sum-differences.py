class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        diff = []
        for i in range(n):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if (left - right ) < 0 :
                diff.append(right - left)
            else :
                diff.append(left - right)
        return diff
        

        