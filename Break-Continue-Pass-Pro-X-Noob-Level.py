# for pig_star in range(10):
#     if pig_star == 7:
#         break
#     print(pig_star)

pig_list = [4, 5, 6]
creeper_list = [10, 20, 30]

for p in pig_list:
    for c in creeper_list:
        if c == 20:
            continue
        print(p * c)
    print("Outside Of Pig/Creeper Powa")
