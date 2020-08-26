n = int(input())

for _ in range(n):
    count = 0
    li = list(map(int,input().strip()))
    mi = min(li)
    length = len(li) 
    for i in range(length):
        if mi in li:
            count += 1
        mi += 1
    if count == length:
        print('YES')
    else:
        print('NO')