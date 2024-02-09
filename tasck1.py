name = str(input("enter your name: "))

name2 = {
    "Darth Vader" : "Luke, I am your father",
    "Leia" : "Luke, I am your sister",
    "Han" : "Luke, I am your brother in law."
}
m = [None]
for x in name2:
    if name == x:
        n = name2[x]
        m.append(n)
        m.remove(None)
        print(m)



