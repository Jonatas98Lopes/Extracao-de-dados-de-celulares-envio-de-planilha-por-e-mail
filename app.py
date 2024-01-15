import openpyxl



workbook = openpyxl.Workbook()
del workbook['Sheet']

workbook.create_sheet('Celulares')
celulares_sheet = workbook['Celulares']
celulares_sheet.append(['Marca', 'Preço'])


