class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        d = nums1 + nums2
        d.sort()
        n = len(d)
        if n % 2 == 1:
            return d[n // 2]
        else:
            return (d[n // 2 - 1] + d[n // 2]) / 2.0