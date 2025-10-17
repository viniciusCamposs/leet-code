class Solution:
    @staticmethod
    def can_construct(ransom_note, magazine):
        for i in set(ransom_note):
            if magazine.count(i) < ransom_note.count(i):
                return False
        return True