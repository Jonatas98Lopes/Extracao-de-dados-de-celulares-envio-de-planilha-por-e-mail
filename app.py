import openpyxl
from acesso_site import extrai_dados_site


workbook = openpyxl.Workbook()
del workbook['Sheet']

workbook.create_sheet('Celulares')
celulares_sheet = workbook['Celulares']
celulares_sheet.append(['Marca', 'Preço($ Dólar)'])

extrai_dados_site(celulares_sheet)
workbook.save('valores_celulares_importados.xlsx')

