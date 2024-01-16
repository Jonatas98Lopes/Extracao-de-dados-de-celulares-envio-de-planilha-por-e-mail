from inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from openpyxl.worksheet.worksheet import Worksheet
import openpyxl
from time import sleep
from enviar_email import *

# Site os dados serão extráidos
SITE = 'https://telefonesimportados.netlify.app/'

# MARCAS E PRECOS contém o DOM da marca e preço de cada celular presente no site.
MARCAS = '//div[@class="single-shop-product"]//h2/a'
PRECOS = '//div[@class="single-shop-product"]//div[@class="product-carousel-price"]/ins'

# Botão que acessa a próxima página do site.
PROXIMA_PAGINA = '//a[@aria-label="Next"]'


def obter_usuario() -> str:
    usuario_email = input("Digite o e-mail para o qual o relatório deve ser enviado: ")
    print(f'O relatório será enviado para o e-mail: {usuario_email}\n')
    return usuario_email



workbook = openpyxl.Workbook()
del workbook['Sheet']

workbook.create_sheet('Celulares')
celulares_sheet = workbook['Celulares']
celulares_sheet.append(['Marca', 'Preço($ Dólar)'])

browser = GoogleChrome()
driver, wait = browser.get_driver(), browser.get_wait()

driver.get(SITE)

usuario_email = obter_usuario()

while True:
    sleep(3)

    driver.execute_script("window.scrollBy(0, 2500);")

    marcas = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, MARCAS)))

    precos = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, PRECOS)))

    # A lógica de adicionar os dados à planilha entra aqui:
    for marca, preco in zip(marcas, precos):
        print('Guardando valores da página atual...')
        nome_marca = marca.text
        valor_preco = preco.text

        celulares_sheet.append([nome_marca, 
            float(valor_preco.split('$')[1])])

    try:
        proxima_pagina = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, PROXIMA_PAGINA)))
        proxima_pagina.click()
        print('\nIndo para a próxima página\n')
    except TimeoutException:
        print('\nChegamos a última página\n')
        driver.quit()
        break

workbook.save('valores_celulares_importados.xlsx')

print('Enviando e-mail...\n')
enviar_email(usuario_email)
print('E-mail enviado com sucesso...')
