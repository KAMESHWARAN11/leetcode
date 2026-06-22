class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        addition = 0
        for i in str(n):
            a = int(i)
            product*= a
            addition += a 
        return product - addition 