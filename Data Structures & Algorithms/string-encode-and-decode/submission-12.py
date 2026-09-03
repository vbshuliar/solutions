class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for s in strs:
            l.append(str(len(s)))
            l.append("#")
            l.append(s)
        return "".join(l)

    
    def decode(self, s: str) -> List[str]:
        strs = []
        c = 0
        w = []
        while c < len(s):
            if s[c].isdigit():
                cur = s[c]
                j = 1
                while s[c+j].isdigit():
                    cur += s[c+j]
                else:
                    c+=j
                for i in range(c+2, int(cur)+c+2):
                    w.append(s[i])
                else:
                    strs.append("".join(w))
                    w.clear()
                    c += int(cur)+2
            else:
                c += 1
        return strs
