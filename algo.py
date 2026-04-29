def min_stations(houses):
    houses.sort()

    stations = []
    i = 0
    n = len(houses)

    while i < n:
        x = houses[i]

        station = x + 4
        stations.append(station)

        while i < n and houses[i] <= station + 4:
            i += 1

    return stations


houses = [1, 2, 3, 8, 9, 14, 18, 19, 20]

stations = min_stations(houses)

print("базовые станции:", stations)
print("минимальное количество:", len(stations))