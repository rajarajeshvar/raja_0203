class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        buckets = [[] for _ in range(len(s)+1)]
        for ch,f in freq.items():
            buckets[f].append(ch)
        result = ""
        for i in range(len(s),0,-1):
            for ch in buckets[i]:
                result += ch * i
        return result