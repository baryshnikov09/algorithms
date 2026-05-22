#30 c)
def max_nezavisimoe_mnozhestvo(vesa):
    n = len(vesa)
    dp = [0] * (n + 1)
    if n == 0:
        return 0, []
    dp[0] = 0
    dp[1] = vesa[0]
    for i in range(2, n + 1):
        ne_berem = dp[i - 1]
        berem = vesa[i - 1] + dp[i - 2]
        dp[i] = max(ne_berem, berem)
    vershiny = []
    i = n
    while i >= 1:
        if i == 1:
            if dp[i] > 0:
                vershiny.append(1)
            break
        ne_berem = dp[i - 1]
        berem = vesa[i - 1] + dp[i - 2]
        if berem > ne_berem:
            vershiny.append(i)
            i -= 2
        else:
            i -= 1
    vershiny.reverse()
    return dp[n], vershiny

vesa = [1, 8, 6, 3, 6]
max_ves, vershiny = max_nezavisimoe_mnozhestvo(vesa)

print("максимальный вес:", max_ves)
print("вершины:", vershiny)