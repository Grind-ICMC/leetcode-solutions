class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            # otimizacao
            if nums[i] > 0:
                break

            # pulando duplicatas
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < target:
                    l += 1
                elif three_sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # pulando duplicatas internas
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    # pulando duplicatas internas
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return res




     


        






        