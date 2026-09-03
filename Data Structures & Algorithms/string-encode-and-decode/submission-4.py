class Solution:

    def encode(self, strs: List[str]) -> str:
        return "%12".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        return s.split("%12")