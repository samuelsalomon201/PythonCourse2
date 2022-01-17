newfile = open("E:/samuel/PythonCourse2/newfile.py", "w+")
newfile.write("#Knock #Knock\n#Whose #there?\n#Joe\n#Joe #Who?\n#Joe #MAMA")
print("TURURURURU")

newfile.seek(0)

print(newfile.read())