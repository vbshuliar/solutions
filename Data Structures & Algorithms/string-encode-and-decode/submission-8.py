class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        return "%12".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        return s.split("%12")