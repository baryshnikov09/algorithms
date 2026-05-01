import itertools

tests = [
    [3/4, 1/2, 1/100],
    [0.9, 0.5, 0.2],
    [0.8, 0.7, 0.6],
    [0.95, 0.4, 0.1],
    [0.99, 0.6, 0.3, 0.05]]

for r in tests:
    print("значения", r)
    best_order = None
    best_sum = -1
    for p in itertools.permutations(r):
        s = 0
        for t, x in enumerate(p):
            s += 100 * x ** (t + 1)
        if s > best_sum:
            best_sum = s
            best_order = p
    print("бест порядок", best_order)
    print("макс выручка", best_sum, "\n")
