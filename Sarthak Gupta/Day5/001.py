class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mod=[*set(nums)]
        cou=[]
        for i in mod:
            count=0
            for j in nums:
                if i==j:
                    count=count+1
            cou.append(count)
        x=cou.index(max(cou))
        return mod[x]
