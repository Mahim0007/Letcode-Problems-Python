class Solution(object):
    def longestCommonPrefix(self,strs):
        prefix=strs[0]
        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix= prefix[:-1]
                if prefix=="":
                    return ""
        return prefix
object=Solution()
print(object.longestCommonPrefix(["flower","flow","flight"]))
