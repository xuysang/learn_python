lst = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]

lst.sort(key=lambda k: k[1])

res = [x[0] for x in lst]

print(lst)
print(res)