class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in d.keys():
                test = d[k]
                test.append(s)
                d[k] = test
            else:
                d[k] = [s]
        return list(d.values())
                