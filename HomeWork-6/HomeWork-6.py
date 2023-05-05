contoset = int(input("Combine\t"))
a = []
b = []
for i in range(contoset):
    t = int(input(f"First tab {i} ...\t"))
    s = int(input(f"Second tab {i} ...\t"))
    a.append(t)
    b.append(s)
print(set(a))
print(set(b))
a = set(a)
b = set(b)
l = a.difference(b), a.union(b), a.intersection(b)
print(l, a == b)
print(f"A difference B:\t{a.difference(b)}")
print(f"B difference A:\t{b.difference(a)}")
print(f"A union B:\t{a.union(b)}")
print(f"A intersection B:\t{a.intersection(b)}")
