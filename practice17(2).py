'''
если цена падает и ri < 1 => раньше надо продавать оборудование, 
которое падает быстрее, то есть у которого коэффициент меньше. 
'''
n = int(input())
r = list(map(float, input().split()))

items = []
for i in range(n):
    items.append((r[i], i + 1))  
items.sort()  

for coef, idx in items:
    print(idx, end=' ')