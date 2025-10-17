from typing import List

class Solution:
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        lst = []
        for idx in range(1, n + 1):
            if idx % 15 == 0:
                lst.append("FizzBuzz")
            elif idx % 3 == 0:
                lst.append("Fizz")
            elif idx % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(idx))
        return lst