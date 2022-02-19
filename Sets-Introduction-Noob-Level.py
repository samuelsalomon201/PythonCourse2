minecraft_xp_mobs_drop = ["Cow", 5, "Chicken", 3, "Horse", 8, "Chicken Jockey", 30]
# '''This Info Is Not True About How Much XP They Drop In Minecraft'''
print(minecraft_xp_mobs_drop)
print(set(minecraft_xp_mobs_drop))

non_related_minecraft_numbers = set([11, 12, 13, 14, 15, 15, 15, 11])
print(non_related_minecraft_numbers)
print(type(non_related_minecraft_numbers))

minecraft_number_of_ores_found = {"Iron Ore", 11, "Gold Ore", 12, "Diamond Ore", 14, "Red Stone Dust Ore", 15,
                                  "Nether Gold Ore", 15, "Copper Ore", 15, "Nether Quarts Ore", 11}
print(minecraft_number_of_ores_found)
print(type(minecraft_number_of_ores_found))

print(11 in minecraft_number_of_ores_found)
print(10 in minecraft_number_of_ores_found)
print(10 not in minecraft_number_of_ores_found)

print(minecraft_number_of_ores_found)

print(minecraft_number_of_ores_found.add("Nether Ore"))
print(minecraft_number_of_ores_found.add("8"))

print(minecraft_number_of_ores_found)

print(minecraft_number_of_ores_found.remove("Iron Ore"))
print(minecraft_number_of_ores_found.remove(11))

print(minecraft_number_of_ores_found)
