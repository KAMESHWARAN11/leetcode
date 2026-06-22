class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0
        for i in operations :
            if i == "++X" or i == "X++" :
                X += 1
            if i == "X--" or i == "--X" :
                X-= 1
        return X
        