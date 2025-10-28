class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final_index = len(digits) - 1

        while True:
            if final_index == -1:
                digits.insert(0, 1)
                break

            final_index_value = digits[final_index]

            final_index_value_plus_one = final_index_value + 1
            if final_index_value_plus_one <= 9:
                digits[final_index] = final_index_value_plus_one
                break

            digits[final_index] = 0
            final_index -= 1

        return digits
