class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        example = min(strs, key=lambda string: len(string))

        equal_char = True
        for idx, character in enumerate(example):
            for string in strs:
                if string[idx] != character:
                    equal_char = False
                    break
            if equal_char:
                prefix += character

        return prefix

