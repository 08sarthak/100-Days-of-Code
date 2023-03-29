class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_co=nums
        count=0
        for i in nums:
            if i!=0:
                nums_co.append(i)
            elif i==0:
                count=count+1
        for j in range(count):
            nums_co.append(0)
        return nums_co
        """
        Do not return anything, modify nums in-place instead.
        """
