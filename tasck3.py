student = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
resulte = []
for x in student.values():
    resulte.append(x)
    resulte.sort()
print(resulte)
