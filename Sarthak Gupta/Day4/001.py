class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[*set(nums)]
        sub=len(nums)-len(res)
        for i in range(sub):
            res.append('_')
        print(res) 
