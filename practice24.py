from collections import defaultdict, deque


def nayti_max_rebro_na_puti(rebra_T, start, finish):
    graf_T = defaultdict(list)
    for i, (u, v, ves) in enumerate(rebra_T):
        graf_T[u].append((v, ves, i))
        graf_T[v].append((u, ves, i))
    ochered = deque([start])
    roditel = {start: None}

    while ochered:
        u = ochered.popleft()
        if u == finish:
            break
        for v, ves, nomer_rebra in graf_T[u]:
            if v not in roditel:
                roditel[v] = (u, ves, nomer_rebra)
                ochered.append(v)

    max_ves = -1
    max_nomer_rebra = None
    tek = finish

    while tek != start:
        pred, ves, nomer_rebra = roditel[tek]
        if ves > max_ves:
            max_ves = ves
            max_nomer_rebra = nomer_rebra
        tek = pred
    return max_ves, max_nomer_rebra


def proverit_MST_posle_dobavleniya(rebra_T, novoe_rebro):
    v, w, c = novoe_rebro
    max_ves, max_nomer_rebra = nayti_max_rebro_na_puti(rebra_T, v, w)

    if c >= max_ves:
        return True
    else:
        return False


def zamenit_MST(rebra_T, novoe_rebro):
    v, w, c = novoe_rebro
    max_ves, max_nomer_rebra = nayti_max_rebro_na_puti(rebra_T, v, w)

    if c >= max_ves:
        return rebra_T
    novoe_T = []
    for i, rebro in enumerate(rebra_T):
        if i != max_nomer_rebra:
            novoe_T.append(rebro)

    novoe_T.append(novoe_rebro)
    return novoe_T

rebra_T = [
    ("A", "B", 4),
    ("B", "C", 2),
    ("C", "D", 5),
    ("B", "D", 7)]
novoe_rebro = ("A", "D", 3)
print(proverit_MST_posle_dobavleniya(rebra_T, novoe_rebro))

novoe_T = zamenit_MST(rebra_T, novoe_rebro)
print(novoe_T)