a = lambda x, y: x * y
print(a)
print(type(a))

print(a(2, 10))
print(a(2, 50))


def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return

print(myfunc([100, 101, 102]))

b = lambda mylist: [x * y for x in range(10) for y in range(5) + mylist]