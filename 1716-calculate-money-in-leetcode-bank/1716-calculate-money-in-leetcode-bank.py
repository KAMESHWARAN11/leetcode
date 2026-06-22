class Solution:
    def totalMoney(self, n: int) -> int:
        week = n//7
        days = n%7
        total = week *28 + (week*(week-1)//2)*7
        for i in range(days):
            total += week+1+i 
        return total
         