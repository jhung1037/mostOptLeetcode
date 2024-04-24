import random


dic = {}
for i in range(1,27):
    dic[i] = chr(96+i)

res = []

num = random.randint(1,10000)
print(num)
lis = []
while num // 10:
    lis.append(num % 10)
    num //= 10
lis.reverse()
dp = [[num]]

for n in lis:
    new = []
    for d in dp:
        if d[-1]<10:
            dd = d[-1]*10+n
            if dd<=26:
                new.append(d[:-1]+[dd])
    if n == 0:
        dp = new
        continue
    
    for d in dp:
        d.append(n)
    dp += new

for d in dp:
    s = ''
    for n in d:
        s += dic[n]

    res.append(s)

print(res)
