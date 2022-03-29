JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = Golden Wing  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"

import re

WAAAWAAAWAAA = re.match("Part 1", JOJOFILES)
print(WAAAWAAAWAAA)
print(type(WAAAWAAAWAAA))

WAAAWAAAWAAA = re.match("AMOGUS", JOJOFILES)
print(WAAAWAAAWAAA)
print(type(WAAAWAAAWAAA))

WAAAWAAAWAAA = re.match("Part 1", JOJOFILES)

print(WAAAWAAAWAAA.group())

WAAAWAAAWAAA = re.match("part 1", JOJOFILES, re.I)
print(WAAAWAAAWAAA)

print(WAAAWAAAWAAA.group())

JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = Golden Wing  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"
WAAAWAAAWAAA = re.match("part 1", JOJOFILES, re.I)
print(WAAAWAAAWAAA)
print(type(WAAAWAAAWAAA))
# WAAWAAWAA = re.search()

while True:
    input(":< ")
