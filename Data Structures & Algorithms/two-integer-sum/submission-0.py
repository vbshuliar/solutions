class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0
        b = len(nums) - 1
        while s < b:
            total = nums[s] + nums[b]
            if total == target:
                return [s, b]
            elif total > target:
                b -= 1
            else:
                s += 1
         