import openpyxl

# print(dir(openpyxl.styles))

from openpyxl.styles import *

workbook = openpyxl.load_workbook("E:\Employees.xlsx")
sheet = workbook['EmployeeData']
cell = sheet['B8']

font = Font(color=colors.BLUE, bold=True, italic=True)

cell.font = font

fill = PatternFill(fill_type='solid', bgColor='E7FE2E')

border = Border(left=Side(border_style='double', color='322FEC'), right=Side(border_style='double', color='322FEC'),
                top=Side(border_style='double', color='322FEC'), bottom=Side(border_style='double', color='322FEC'))

cell.border = border

align = Alignment(horizontal='left')

cell.alignment=align

workbook.save("E:Empoyees.xlsx")
