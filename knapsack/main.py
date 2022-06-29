from time import time

w = [8,3,5,2]
W = 9
p = [16,8,9,6]

def backpack(w, p, W, currentValue=0, currentWeight=0, res=[]):
    if len(w) == 0:
        if currentWeight > W:
            return (0,0,0)
        return (currentValue, currentWeight, res)
    return max(
        backpack(w[1:], p[1:], W, currentValue, currentWeight, res + [0]),
        backpack(w[1:], p[1:], W, currentValue + p[0], currentWeight + w[0], res + [1]),
        key=lambda item: item[0])

def backpackHeuristic(w, p, W):
    sortedItems = sorted(list(zip(p,w)), key=lambda item: item[0] / item[1], reverse=True)

    totalWeight = 0
    totalValue = 0
    items = []

    for value, weight in sortedItems:
        if totalWeight + weight <= W:
            totalWeight += weight
            totalValue += value
            items.append((value, weight))

    res = []
    for item in zip(p, w):
        if item in items:
           res.append(1)
        else:
           res.append(0)
    return (totalValue, totalWeight, res)


currentTime = time()
print(backpack(
    [96, 49, 60, 16, 73, 15, 11, 39, 80, 13, 86, 47, 33, 96, 22, 22, 97, 27, 92, 1, 33, 47],
    [78, 58, 1, 17, 7, 13, 53, 72, 42, 68, 37, 58, 13, 15, 60, 83, 61, 45, 23, 61, 78, 15],
    500))
print(time() - currentTime)



# Odpowiedzi na pytania:
# Czy uzyskano takie same rozwiązania?
#     Nie
# Jakie wnioski można z tego wyciągnąć?
#     Rozwiązanie problem przy użyciu heurystyki pozwalia znacząco przyspieszyć działanie funkcji, ale nie gwarantuje otrzymanie najlepszego wyniku
# Jak dużą instancję problemu (liczba przedmiotów) da się rozwiązać w około minutę metodą zachłanną?
#     21 przedmoit za 49 sekund na laptopie z procesorem i5-8300h
# Jak bardzo wydłuży obliczenia dodanie jeszcze jednego przedmiotu?
#     do 96 sekund, czyli prawie dwukrotnie

