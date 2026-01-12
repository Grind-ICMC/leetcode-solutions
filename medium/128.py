class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                lenght = 1
                curr = num

                while curr + 1 in nums_set:
                    curr += 1
                    lenght += 1

                res = max(res, lenght)

        return res




        
        