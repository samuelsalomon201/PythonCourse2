list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
list2 = [-11, 2, 12]
print(min(list2))
print(max(list2))
list3 = ["a", "b", "c"]
print(min(list3))
print(max(list3))
print(list1)
list1.append(100)
print(list1)
del list1[4]
print(list1)
list1.pop(0)
print(list1)
list1.remove("Juniper")
print(list1)
list1.insert(2, "Nortel")
print(list1)
list2 = [9, 99, 999]
print(list1)
print(list2)
list1.extend(list2)
print(list1)
print(list1.index(-11))
list1.append(10)
print(list1)
print(list1.count(10))
print(list2)
list2.append(1)
list2.append(25)
list2.append(500)
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(sorted(list2))
print(sorted(list2, reverse = True))
print(list1 + list2)
print(list2 * 3)