import openpyxl

workbook = openpyxl.load_workbook("E:\Employees.xlsx")
print(workbook.properties)
print(workbook.sheetnames)
print(workbook.active)
sheet = workbook['EmployeeData']
workbook.create_sheet('TestSheet')
workbook.save("E:\Employees.xlsx")

sheet = workbook['TestSheet']
workbook.remove(sheet)

workbook.save("E:\Employees.xlsx")

workbook.close()
