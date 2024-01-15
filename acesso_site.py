from inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from time import sleep


# Site os dados serão extráidos
SITE = 'https://telefonesimportados.netlify.app/'

# MARCAS E PRECOS contém o DOM da marca e preço de cada celular presente no site.
MARCAS = '//div[@class="single-shop-product"]//h2/a'
PRECOS = '//div[@class="single-shop-product"]//div[@class="product-carousel-price"]/ins'

# Botão que acessa a próxima página do site.
PROXIMA_PAGINA = '//a[@aria-label="Next"]'

browser = GoogleChrome()
driver, wait = browser.get_driver(), browser.get_wait()


driver.get(SITE)

while True:
    sleep(3)

    driver.execute_script("window.scrollBy(0, 2500);")

    marcas = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, MARCAS)))

    precos = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, PRECOS)))

    # A lógica de adicionar os dados à planilha entra aqui:
    for marca, preco in zip(marcas, precos):
        print(marca.text + " " + preco.text)

    try:
        proxima_pagina = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, PROXIMA_PAGINA)))
        proxima_pagina.click()
    except TimeoutException:
        break
print("Acabamos")
    





