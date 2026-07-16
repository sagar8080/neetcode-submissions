class Solution:

    def encode(self, strs: List[str]) -> str:
        self.token = "<tok>"
        if not strs:
            return ""
        encoded_string = ""
        for string in strs:
            encoded_string += string + self.token
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = s.split(self.token)
        return result[:-1]