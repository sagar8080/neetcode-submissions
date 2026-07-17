class Solution:
    def __init__(self):
        self.salt = "%^@"
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if strs:
            for s in strs:
                encoded_str += self.salt + s
            return encoded_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        chars = s.split(self.salt)[1:]
        return chars
