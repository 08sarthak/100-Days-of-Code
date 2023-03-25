class Solution(object):
    def twoSum(self, nums, target):
        out=[]
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    out.append(i)
                    out.append(j)
                    count=1
            if count==1:
                break
        return out
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
