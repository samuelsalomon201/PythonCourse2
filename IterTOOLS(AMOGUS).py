from itertools import *

luck = [1, 2, 3, 'a', ' b,' 'c']
# &
pluck = [101, 102, 103, 'X', 'Y']

print(chain(luck, pluck))

for sus in chain(luck, pluck):
    print(sus)

print(list(chain(luck, pluck)))

for amogus in count(10, 2.5):
    if amogus <= 50:
        print(amogus)
    else:
        break

# Infinite Loop (Not True Tho)
# corn = range(11, 16)
# for dahub in cycle(corn):
#     print(dahub)

print(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7]))

print(list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])))
