from typing import List

class Solution:
    @staticmethod
    def running_sum(nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums