from typing import List

class Solution:
    @staticmethod
    def maximum_wealth(accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)