def my_wrapper(candy):
    def sussy_wrapper():
        return "Amogus is" + candy() + "sussy!"
    return sussy_wrapper()

@my_wrapper
def candy():
    return " Very "
