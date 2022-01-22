list1 = [x ** 2 for x in range(10)]
print(list1)

list2 = [x ** 2 for x in range(10) if x >5]
print(list2)

set1 = {x ** 2 for x in range(10)}
print(set1)
print(type(set1))

dick1 = {x : x * 2 for x in range(10)}
print(dick1)
print(type(dick1))