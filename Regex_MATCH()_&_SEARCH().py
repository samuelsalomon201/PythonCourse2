JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = El Vento De Oro  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"

import re

SUUUS = re.match("Part 1", JOJOFILES)
print(SUUUS)
print(type(SUUUS))

SUUUS = re.match("A-MOM-GUS", JOJOFILES)
print(SUUUS)
print(type(SUUUS))

SUUUS = re.match("Part 1", JOJOFILES)

print(SUUUS.group())

SUUUS = re.match("part 1", JOJOFILES, re.I)
print(SUUUS)

print(SUUUS.group())

JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = El Vento De Oro  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"
SUUUS = re.match("part 1", JOJOFILES, re.I)
print(SUUUS)
print(type(SUUUS))
# SUUUS = re.search()

while True:
    input("*** ")
