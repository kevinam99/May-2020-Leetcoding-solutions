class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for note in set(ransomNote): # to get unique elements
            if not ransomNote.count(note) <= magazine.count(note):
                return False
        
        return True