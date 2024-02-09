dict2 = [
    {"x": -2, "y": 1},
    {"x": 4, "y": 3}
]
resulte = 0
for x in dict2:
    for y in x.values():
        p = y ** 2
        resulte += p
print(resulte)