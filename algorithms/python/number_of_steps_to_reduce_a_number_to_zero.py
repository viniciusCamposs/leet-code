class Solution:
    def number_of_steps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if self.is_even(num):
                num = num / 2
            else:
                num = num -1
            steps += 1

        return steps

    @staticmethod
    def is_even(num: int) -> int:
        return num % 2 == 0