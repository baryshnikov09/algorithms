def dfs(obrazec):
    for drugoi_obrazec, tip_svyazi in graf_svyazei[obrazec]:
        nuzhnyi_vid = vid_babochki[obrazec] ^ tip_svyazi

        if vid_babochki[drugoi_obrazec] == -1:
            vid_babochki[drugoi_obrazec] = nuzhnyi_vid
            if not dfs(drugoi_obrazec):
                return False
        else:
            if vid_babochki[drugoi_obrazec] != nuzhnyi_vid:
                return False
    return True


kolvo_obrazcov, kolvo_ocenok = map(int, input().split())
graf_svyazei = [[] for _ in range(kolvo_obrazcov + 1)]

for _ in range(kolvo_ocenok):
    pervyi_obrazec, vtoroi_obrazec, ocenka = input().split()
    pervyi_obrazec = int(pervyi_obrazec)
    vtoroi_obrazec = int(vtoroi_obrazec)

    if ocenka == "same":
        tip_svyazi = 0
    else:
        tip_svyazi = 1

    graf_svyazei[pervyi_obrazec].append((vtoroi_obrazec, tip_svyazi))
    graf_svyazei[vtoroi_obrazec].append((pervyi_obrazec, tip_svyazi))

vid_babochki = [-1] * (kolvo_obrazcov + 1)
answer = True

for obrazec in range(1, kolvo_obrazcov + 1):
    if vid_babochki[obrazec] == -1:
        vid_babochki[obrazec] = 0
        if not dfs(obrazec):
            answer = False
            break

if answer:
    print("Да")
else:
    print("Нет")