myfile = open("E:\TURURURURU.txt", "r")

print(myfile.mode)

print(myfile.read(12))
print(myfile.read(1))
print(myfile.read(2))
print(myfile.read(3))
print(myfile.read(0))
print(myfile.read(7))
print(myfile.readlines())
print(myfile.seek(0))

for line in myfile.readlines():
    if line.startswith("a"):
        print(line)
