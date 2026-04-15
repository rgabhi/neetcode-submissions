class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict()
        for s in strs:
            key = sorted(s)
            key = ''.join(key)
            # print(key)
            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)
        return [x for x in hm.values()]