def candy(candy_wrapper):
    def candy_inside():
        return "Candy is such a " + candy_wrapper() + " thing"
    return candy_inside()

@candy
def candy_wrapper():
    return "SUSSY"

print(candy_wrapper)