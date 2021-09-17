# Sort Integers - Factors Count
# The program must accept N integers, arr[i] where i is from 0 to N-1 and print the integers based on the number of factors in descending order. If multiple integers have the same number of factors, then they must be printed in the same line sorted in descending order.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= arr[i] <= 10000

# Input Format:
# The first line contains N.
# The second line contains the N integer values separated by a space.

# Output Format:
# Several lines contain the N integer values.

# Example Input/Output 1:
# Input:
# 5
# 10 5 7 8 99

# Output:
# 99
# 10 8
# 7 5

# Explanation:
# Here N=5 and the given 5 integers are 10 5 7 8 99.
# The number of factors of 10 is 4 (1, 2, 5, 10).
# The number of factors of 5 is 2 (1, 5).
# The number of factors of 7 is 2 (1, 7).
# The number of factors of 8 is 4 (1, 2, 4, 8).
# The number of factors of 99 is 6 (1, 3, 9, 11, 33, 99).
# The given 5 integers are printed based on the number of factors in descending order as below.
# 99
# 10 8
# 7 5

# Example Input/Output 2:
# Input:
# 4
# 2 3 5 7

# Output:
# 7 5 3 2


n=int(input())
arr=list(map(int,input().split()))
dic={}
def factors(i):
    count=0
    for el in range(1,i+1):
        if i%el==0:
            count+=1 
    return count

for i in arr:
    c=factors(i) 
    dic[c]=dic.get(c,[])+[i]
for i in sorted(dic.keys(),reverse=True):
    print(*sorted(dic[i],reverse=True))
    