class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            count=0
            for j in nums:
                if(i==j):
                    count+=1
            if(count==1):
                return i
