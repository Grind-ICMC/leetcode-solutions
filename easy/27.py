class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        trash = len(nums) - k

        for _ in range(trash):
            nums.pop()

        return k

        

