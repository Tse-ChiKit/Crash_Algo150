from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        read = 2
        write = 2

        while read < len(nums):
            if nums[read] == nums[write - 2]:
                read += 1
            else:
                nums[write] = nums[read]
                read += 1
                write += 1

        return write
