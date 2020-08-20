def check(li):
    op = 0
    cl = 0
    for i in li:
        if i == '(':
            op += 1
        elif i == ')':
            cl += 1
    if op == cl:
        return True
    else:
        return False


li = list(input().strip())
flag = 0
if check(li):
    l = ['#']
    c = 0
    for item in li:
        if item == '(':
            l.append(item)
        elif item == ')':
            if l[-1] == '#':
                c = 0
                flag = 1
            else:
                l.pop()
                if l[-1] == '#':
                    c += 1
    if flag:
        print(c+1)
    else:
        print(c)
else:
    print(0)


#[ #,    ]




"""
a = [#,),]

)()()(
"""
