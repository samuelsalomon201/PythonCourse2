boom_range = range(10)

for i in boom_range:
    print(i * 2)


night_mobs = ["Zombie", "Skeleton", "Creeper", "Spider", "Ender Man"]
print(len(night_mobs))

print(list(range(5)))
for element_index in range(len(night_mobs)):
    print(night_mobs[element_index])

for index, number in enumerate(night_mobs):
    print(index, number)

for element in night_mobs:
    print(element)
else:
    print("The End Of The List Has Been Reached")

