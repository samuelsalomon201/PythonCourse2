minecraft_dick = {"Mojang": "Minecraft", "Pig": "Creeper", "Version": "1.18", "Year": "2011"}
print(minecraft_dick)
print(minecraft_dick["Pig"])
print(minecraft_dick["Mojang"])
minecraft_dick["Biome"] = "Ocean Biome"
print(minecraft_dick)
minecraft_dick["Version"] = "1.16.5"
print(minecraft_dick)
del minecraft_dick["Year"]
print(minecraft_dick)
print(len(minecraft_dick))

print("Mojang" in minecraft_dick)
print("Mojan" in minecraft_dick)
print("Mojan" not in minecraft_dick)
print(minecraft_dick.keys())
print(minecraft_dick.values())
print(minecraft_dick.items())
print(type(minecraft_dick.keys()))
print(type(minecraft_dick.values()))
print(type(minecraft_dick.items()))
print(list(minecraft_dick.keys()))
print(list(minecraft_dick.values()))
print(list(minecraft_dick.items()))
