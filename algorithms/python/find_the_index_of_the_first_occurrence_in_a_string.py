class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        needle_length = len(needle)
        for index in range(len(haystack)):
            if haystack[index:needle_length + index] == needle:
                return index

        return -1