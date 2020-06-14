t = int(input())

for test in range(t):
    count = 0
    n = int(input())
    st = input()
    for i in range(n):
        try:
            if st[i+1] in "aeiou":
                if not(st[i] in "aeiou"):
                    count+=1
        except:
            break
    print(count)
