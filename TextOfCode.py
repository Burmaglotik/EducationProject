'''typeRoom = input()
if typeRoom == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif typeRoom == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif typeRoom == 'круг':
    r = float(input())
    print(3.14 * r * r)


a = int(input())
b = int(input())
c = int(input())
maxOf = b
minOf = a
if a >= b:
    maxOf = a
    minOf = b
if c >= maxOf:
    print(c)
    print(minOf)
    print(maxOf)
else:
    print(maxOf)
    if (c <= minOf):
        print(c)
        print(minOf)
    else:
        print(minOf)
        print(c)


n = int(input())
if 0 <= n <= 1000:
    if (n % 10 == 0 or 5 <= n % 10 <= 9 or 11 <= n % 100 <= 14):
        print (n,'программистов')
    elif n % 10 == 1:
        print(n, 'программист')
    elif 2 <= n % 10 <= 4:
        print (n, 'программиста')


ticket = int(input())
a = ticket // 100000
b = ticket // 10000 - a * 10
c = ticket // 1000 - a * 100 - b * 10
d = ticket // 100 - a * 1000 - b * 100 - c * 10
e = ticket // 10 - a * 10000 - b * 1000 - c * 100 - d * 10
f = ticket % 10
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')


s = 0
i = 1
while i != 0:
    i = int(input())
    s += i
print(s)


a = int(input())
b = int(input())
d = 1
while not (d % a == 0 and d % b == 0):
    d += 1
print(d)



while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    else:
        print(num)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()


a = int(input())
b = int(input())
s = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        count += 1
print(s / count)



sostav = input()
print((sostav.lower().count('g') + sostav.lower().count('c')) * 100 / len(sostav))
'''


gna = input()
i = 0
while i < len(gna):
    cnt = 1
    for j in range(i + 1, len(gna)):
        if gna[j] == gna[i]:
            cnt += 1
        else:
            break
    if cnt > 1:
        print(gna[i], end='')
        print(cnt, end='')
        i += cnt
    else:
        print(gna[i], end='')
        print(cnt, end='')
        i += 1

