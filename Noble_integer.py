def findInteger(A):
    A.sort(reverse=True)
    cnt=[0]
    curr=0
    for i in range(1,len(A)):
        if A[i-1]!=A[i]:
            cnt.append(i)
            curr=i
        else:
            cnt.append(curr)
    print(cnt)
    for i in range(len(A)):
        if A[i]==cnt[i]:
            return 1
    return -1
A=list(map(int,input().split()))
print(findInteger(A))

"""
Input 1:
A = [3, 2, 1, 3]

Input 2:
A = [1, 1, 3, 3]


Output 1:
1

Output 2:
-1
"""





    


