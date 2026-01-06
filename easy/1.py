# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add_to = {}

        for i, n in enumerate(nums): # 0, 1
            diff = target - n # 7, 2
            
            if diff in add_to:
                return [add_to[diff], i] # 0, 1

            add_to[n] = i # 2 -> 0






