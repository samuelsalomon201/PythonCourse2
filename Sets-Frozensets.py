list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]
fs1 = frozenset(list1)
fs2 = frozenset(list2)
print(fs1)
print(fs2)
print(type(fs1))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.union(fs2))