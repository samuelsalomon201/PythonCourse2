x = "Cisco"
y = " Switch"
print(x + y)
print(x * 3)
print(x)
print("o" in x)
print("b" in x)
print("b" not in x)
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2691XM", 4, 12.3))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("7200XR", 8, 15.4))


print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4))


print("Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4))


print("Cisco model: {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4))

model = '2600XM'
slots = 4
ios = 12.3

print(f"Cisco model: {model}, {slots} Wan slots, IOS {ios}")

print(f"Cisco model: {model}, {slots * 2} Wan slots, IOS {ios}")

print(f"Cisco model: {model.lower()}, {slots * 2} Wan slots, IOS {ios}")