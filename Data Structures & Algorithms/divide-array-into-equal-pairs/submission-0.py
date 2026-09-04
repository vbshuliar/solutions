class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        short = set(nums)
        for n in short:
            if nums.count(n) % 2 != 0:
                return False
        return True