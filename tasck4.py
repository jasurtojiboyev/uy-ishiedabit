Scrable = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
resulte = 0
for x in Scrable:
    for y in x.values():
        m = x["score"]
    resulte += m
print(resulte)
