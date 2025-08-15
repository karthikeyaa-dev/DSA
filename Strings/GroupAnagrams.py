from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
            
        return list(anagrams.values())
        