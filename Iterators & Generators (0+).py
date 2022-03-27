my_list = [1, 2, 3, 4, 5, 6, 7]
my_iter = iter(my_list)
next(my_iter)


def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y


my_object = my_gen(10, 5)
next(my_object)
gen_exp = (x for x in range(5))
next(gen_exp)
