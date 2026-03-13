class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in strs:
            k = ''.join(sorted(w))
            if k not in d:
                d[k] = []
            d[k].append(w)

        return list(d.values())