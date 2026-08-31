class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lego = set(nums)
        longest = 0
        for n in lego:
            if n - 1 not in lego:
                count = 1

                while n + count in lego:
                    count += 1
                longest = max(longest, count)

        return longest



        