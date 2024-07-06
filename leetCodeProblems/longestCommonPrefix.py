'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string

'''
class Solution :
    def longestCommonPrefix(self, strs):
        if not strs:#this will return 0 if strs is empty
            return ""
        
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]

        return pref

    