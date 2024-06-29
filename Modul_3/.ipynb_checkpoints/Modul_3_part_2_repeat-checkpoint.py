L = [1, 4, 1, 6, "hello", "a", 5, "hello"]
L = list(map(str, L))
L.sort()
D = []
for i in range(1,len(L)):
    if L[i] == L[i-1]:
        D.append(L[i])
print('Повторяющиеся значения:', D)