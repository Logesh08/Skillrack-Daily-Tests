# Split Palindromes
# The program must accept a string S as the input. The string S is not a palindrome but it is formed by concatenating two palindromes. The program must split the string S into two palindromes and print the palindromes in separate lines as the output.

# Boundary Condition(s):
# 2 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains a string value representing the first palindrome.
# The second line contains a string value representing the second palindrome.

# Example Input/Output 1:
# Input:
# madamabba

# Output:
# madam
# abba

# Explanation:
# Here the given string is madamabba.
# The string values madam and abba are palindrome, so madam and abba are printed in separate lines.

# Example Input/Output 2:
# Input:
# eyerotator

# Output:
# eye
# rotator

# Example Input/Output 3:
# Input:
# aaaababa

# Output:
# aaa
# ababa


s=input().strip()
r = s[::-1]
for i in range(2,len(s)):
    x,y = s[:i],s[i-1::-1]
    if x==y:
        for j in range(2,len(s)):
            a,b = r[:j],r[j-1::-1]
            if a==b:
                print(s[:i],s[i:],sep='\n')
                exit()