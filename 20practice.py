def optimalnyi_poryadok_triatlon(uchastniki):

    uchastniki.sort(key=lambda x: x[2] + x[3], reverse=True)

    vremya_basseina = 0
    zavershayushee_vremya = 0

    for imya, plavanie, velosiped, beg in uchastniki:
        vremya_basseina += plavanie
        finish_uchastnika = vremya_basseina + velosiped + beg
        zavershayushee_vremya = max(zavershayushee_vremya, finish_uchastnika)

    return uchastniki, zavershayushee_vremya


uchastniki = [
    ("A", 3, 10, 5),
    ("B", 4, 2, 2),
    ("C", 2, 8, 7)]

poryadok, vremya = optimalnyi_poryadok_triatlon(uchastniki)

print("оптимальный порядок:")
for uchastnik in poryadok:
    print(uchastnik[0])

print("минимально завершенное время:", vremya)