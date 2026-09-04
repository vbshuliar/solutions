class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1
                current = n

                while current + 1 in nums:
                    current += 1
                    length += 1
                
                m = max(m, length)
        return m