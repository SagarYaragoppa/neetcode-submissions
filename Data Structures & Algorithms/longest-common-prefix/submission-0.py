class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        r = strs[0]
        x = 1
        while x <= len(r):
            prefix = r[:x]

            if all(word.startswith(prefix) for word in strs):
                x += 1
            else:
                break

        return r[:x-1]