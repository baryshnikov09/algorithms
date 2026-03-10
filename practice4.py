left_v, left_r = 5, 5

g = [[0],
     [0, 1],
     [1, 2],
     [2, 3],
     [3, 4]]
match = [-1] * left_r
used = [0] * left_v

def obhod_v_glubinu(v):
    if used[v] == 1:
        return False
    used[v] = 1
    for kuda_idem in g[v]:
        if match[kuda_idem] == -1 or obhod_v_glubinu(match[kuda_idem]):
            match[kuda_idem] = v
            return True
    return False

for v in range(left_v):
    used = [0] * left_v
    obhod_v_glubinu(v)

for y in range(left_r):
    if match[y] != -1:
        print(f"x{match[y]} - y{y}")