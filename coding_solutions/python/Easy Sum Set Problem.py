a = int(input())
A=list(map(int,input().split()))
c = int(input())
C=list(map(int,input().split()))
li= []
ans = []
z=0
for i in range(c):
    for j in range(a):
        ele = C[i] - A[j]
        li.append(C[i]-A[j])
        for k in range(a):
            if (ele + A[k]) in C:
                z+=1
        if z == a:
            print(ele)
            ans.append(ele)

        z = 0
print(set(ans))

for i in sorted(set(ans)):
    print(i , end=" ")



