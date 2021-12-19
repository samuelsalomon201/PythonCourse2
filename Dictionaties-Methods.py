dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": 4}
print(dict1)
print(dict1["IOS"])
print(dict1["Vendor"])
dict1["RAM"] = "128"
print(dict1)
dict1["IOS"] = "12.3"
print(dict1)
del dict1["Ports"]
print(dict1)
print(len(dict1))
print("IOS" in dict1)
print("IOS2" in dict1)
print("IOS2" not in dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(type(dict1.keys()))
print(type(dict1.values()))
print(type(dict1.items()))
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))