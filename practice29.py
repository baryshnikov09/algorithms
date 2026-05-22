from bisect import bisect_left


def maksimalnaya_pribyl_shity(x, r):
    tochki = sorted(zip(x, r))
    x = [tochka[0] for tochka in tochki]
    r = [tochka[1] for tochka in tochki]
    n = len(x)
    pred = [0] * n

    for j in range(n):
        granica = x[j] - 5
        i = bisect_left(x, granica) - 1
        pred[j] = i
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        bez_j = dp[j - 1]
        s_j = r[j - 1] + dp[pred[j - 1] + 1]
        dp[j] = max(bez_j, s_j)
    return dp[n]

x = [6, 7, 12, 14]
r = [5, 6, 5, 1]

print(maksimalnaya_pribyl_shity(x, r))