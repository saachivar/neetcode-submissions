class Solution:

    def encode(self, strs: List[str]) -> str:
        megastring = ""
        for string in strs:
            megastring+=str((len(string)))+"#"
            megastring+=string
        return megastring

    def decode(self, s: str) -> List[str]:
        string_array = []
        i = 0
        while i < len(s):
            length = int(s[i:].split("#")[0])
            j = s.find("#", i)
            string_array.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return string_array

            
