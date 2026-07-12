class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                v = v+1
        for j in range(len(nums)):
            for i in range(0,len(nums)):
                if nums[i] == "_" and i!=len(nums)-1:
                    nums[i] = nums[i+1]
                    nums[i+1] = "_"
        return len(nums) - v