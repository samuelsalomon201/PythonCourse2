JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = Golden Wing  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"

import re

WAAWAAWAA = re.match("Part 1", JOJOFILES)
print(WAAWAAWAA)
print(type(WAAWAAWAA))

WAAWAAWAA = re.match("AMOGUS", JOJOFILES)
print(WAAWAAWAA)
print(type(WAAWAAWAA))

WAAWAAWAA = re.match("Part 1", JOJOFILES)

print(WAAWAAWAA.group())

WAAWAAWAA = re.match("part 1", JOJOFILES, re.I)
print(WAAWAAWAA)

print(WAAWAAWAA.group())

JOJOFILES = "Part 1 = Phantom Blood Part 2 = Battle Tendency Part 3 = Stardust Crusaders Part 4 = Diamond Is Unbreakable" \
            " Part 5 = Golden Wing  Part 6 = Jojo Stone Ocean Part 7 = Steel Ball Run Part 8 = Jojolion"
WAAWAAWAA = re.match("part 1", JOJOFILES, re.I)
WAAWAAWAA
print(type(WAAWAAWAA))
# WAAWAAWAA = re.search()
