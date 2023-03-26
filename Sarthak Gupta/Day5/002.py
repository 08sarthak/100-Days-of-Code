class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mod=[*set(nums)]
        if len(nums)!=len(mod):
            x=True
        else:
            x=False
        return x
