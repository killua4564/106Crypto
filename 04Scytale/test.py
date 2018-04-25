flag = open('test', 'r').read()
n = 4
a = ['' for i in range(n)]
for i in range(len(flag)):
    a[i % n] += flag[i]
print(''.join(a))