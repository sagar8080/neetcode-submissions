class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocessing
        character_list = []
        for ch in s:
            if ch.isalnum():
                character_list.append(ch)
        
        l, r = 0, len(character_list) - 1
        print(character_list)
        while l <= r:
            if character_list[l].lower() != character_list[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True