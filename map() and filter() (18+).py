def product10(a):
    return a * 10

r1 = range(10)

print(map(product10, r1))
print(list(map(product10, r1)))

print(map((lambda a: a * 10), r1))
# print(list(map(lambda a: a * 10), r1))

filter((lambda a: a > 5), r1)
list(filter((lambda a: a > 5), r1))
