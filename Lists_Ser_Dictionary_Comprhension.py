"""Super Efficient Way"""
corn = []

for PP in range(10):
    Hub = PP ** 2
    corn.append(Hub)

print(corn)

"""Un-Efficient Way"""
fakecorn = [Hub ** 2 for Hub in range(10)]

print(fakecorn)

"""Mid Efficient Way"""
realcorn = [Hub ** 2 for Hub in range(10) if Hub > 5]
print(realcorn)

"""LOL Wat Is SAUS"""
sus1 = {SAUS ** 2 for SAUS in range(10)}
print(sus1)
print(type(sus1))

"""Amogusmogus LOL"""
Amogusmogus = {E: E * 2 for E in range(10)}
print(Amogusmogus)
print(type(Amogusmogus))
