def my_first_function(x, y, z):
    sum_xyz = (x + y) * z
    return sum_xyz

# my_first_function(1, 2)

print(my_first_function(x = 1, y = 2, z = 3))

print(my_first_function(z = 3, x = 1, y = 2))

# print(my_first_function(x = 1, y = 2, 3))

print(my_first_function(1, 2, 3))

print(my_first_function(1, 2, z = 3))

print(my_first_function(10, 12, z = 3))

print(my_first_function(110, 120, z = 3))

def my_first_function(x, y, z = 3):
    sum_xyz = (x + y) * z
    return sum_xyz

print(my_first_function(1, 2))

print(my_first_function(1, 2, 4))


def function1(x, *args):
    print(x)

print(function1("hell o wip"))

def function1(x, *args):
    print(x)
    print(args)

print(function1("hell o wip"))

print(function1("hell o wip", 100, 200))

def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)

print(function1(1, 2, 3))

# **kwards