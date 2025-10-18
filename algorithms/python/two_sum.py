from typing import List

class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for nested_idx, nested_num in enumerate(nums):
                if idx == nested_idx:
                    continue

                if num + nested_num == target:
                    return [idx, nested_idx]

        return []