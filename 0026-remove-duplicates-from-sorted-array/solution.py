from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 1
        write = 1

        while read < len(nums):
            if nums[read] == nums[write - 1]:
                read += 1
            else:
                nums[write] = nums[read]
                read += 1
                write += 1

        return write
