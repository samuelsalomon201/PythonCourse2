minecraft_test_pig = {1, 2, 3, 4}
minecraft_test_pig_fail = {3, 5, 8}

print(minecraft_test_pig.intersection(minecraft_test_pig_fail))
print(minecraft_test_pig_fail.intersection(minecraft_test_pig))
print(minecraft_test_pig.difference(minecraft_test_pig_fail))
print(minecraft_test_pig_fail.difference(minecraft_test_pig))
print(minecraft_test_pig.union(minecraft_test_pig_fail))
print(minecraft_test_pig)
print(minecraft_test_pig.pop())
print(minecraft_test_pig)
minecraft_test_pig.clear()
print(minecraft_test_pig)