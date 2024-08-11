'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

# Example to check the output
solution = Solution()
test_string = "Hello World"
output = solution.lengthOfLastWord(test_string)
print(f"Output for '{test_string}': {output}")
