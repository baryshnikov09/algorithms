m, n = map(int, input().split())

s1 = input().split()   # S' длины m
s2 = input().split()   # S длины n

i = 0
j = 0

while i < m and j < n:
    if s1[i] == s2[j]:
        i += 1
    j += 1

if i == m:
    print("является подпоследовательностью")
else:
    print("не является подпоследовательностью")