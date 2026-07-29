#  Smallest Palindromic Rearrangement I

# You are given a palindromic string s.

# Return the lexicographically smallest palindromic permutation of s.

 

# Example 1:

# Input: s = "z"

# Output: "z"

# Explanation:

# A string of only one character is already the lexicographically smallest palindrome.

# Example 2:

# Input: s = "babab"

# Output: "abbba"

# Explanation:

# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.



class Solution:
    def smallestPalindrome(s):
        x=len(s)//2
        start_string =sorted(s[:x])
        mid=[s[x]] if len(s) % 2 == 1 else []
        end_string = start_string[::-1]
        result=''.join(start_string + mid + end_string)
        return print(result)

Solution.smallestPalindrome('z')
Solution.smallestPalindrome('babab')
Solution.smallestPalindrome('adcacd')

     
    