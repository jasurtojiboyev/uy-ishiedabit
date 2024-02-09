name_budget = [
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]
resulte = 0
for x in name_budget:
    for y in x.values():
        m = x["budget"]
    resulte += m
print(resulte)