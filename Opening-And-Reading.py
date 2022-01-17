myfile = open("E:/samuel/PythonCourse2/Opening-And-Reading-List.py", "r")

print(myfile.mode)

print(myfile.read())

print(myfile.seek(0))
print(myfile.tell())

print(myfile.read(6))
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

print(myfile.seek(0))

for line in myfile.readlines():
    if line.startswith("A"):
        print(line)

# myfile = open("E:/samuel/PythonCourse2/Opening-And-Reading-List.py", "x")