class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        final_word = s.strip().split(" ")[-1]

        return len(final_word)
