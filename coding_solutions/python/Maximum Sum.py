n = int(input())
arr = list(map(int,input().split()))
ans = []

for i in arr:
    if i >= 0:
        ans.append(i)
if len(ans) != 0:
    print(sum(ans),end=" ")
    print(len(ans))
else:
    print(max(arr),end=" 1")
