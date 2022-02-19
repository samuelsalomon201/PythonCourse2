minecraft_pig_spawn_family_size = [1, 2, 3, 4]
minecraft_other_rare_pig_spawn_family_size = [3, 4, 7]

frozen_pig_mod = frozenset(minecraft_pig_spawn_family_size)
frozen_pig_mod_for_old_versions = frozenset(minecraft_other_rare_pig_spawn_family_size)

print(frozen_pig_mod)
print(frozen_pig_mod_for_old_versions)
print(type(frozen_pig_mod))
print(type(frozen_pig_mod_for_old_versions))

# frozen_pig_mod.add(10)

# frozen_pig_mod.remove(1)

# frozen_pig_mod.pop()

# frozen_pig_mod.clear()

print(frozen_pig_mod)


print(frozen_pig_mod.intersection(frozen_pig_mod_for_old_versions))
print(frozen_pig_mod.difference(frozen_pig_mod_for_old_versions))
print(frozen_pig_mod.union(frozen_pig_mod_for_old_versions))
