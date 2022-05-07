import openpyxl

print(dir(openpyxl.styles))
openpyxl.styles.Border
workbook = openpyxl.load_workbook("E:\samuel\Employees.xlsx")
sheet = workbook['EmployeeData']
cell = sheet['C10']

# font = Font(color = colors.RED, bold = True, italic = True)
