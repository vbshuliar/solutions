class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            search = target-n
            if search in d.keys():
                return [d[search], i]
            d[n] = i
        return []
         