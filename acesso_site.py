from inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep


# Site os dados serão extráidos
SITE = 'https://telefonesimportados.netlify.app/'

# MARCAS E PRECOS contém o DOM da marca e preço de cada celular presente no site.
MARCAS = '//div[@class="single-shop-product"]//h2/a'
PRECOS = '//div[@class="single-shop-product"]//div[@class="product-carousel-price"]/ins'

browser = GoogleChrome()
driver, wait = browser.get_driver(), browser.get_wait()


driver.get(SITE)
sleep(5)

driver.execute_script("window.scrollBy(0, 2500);")

marcas = wait.until(expected_conditions.visibility_of_all_elements_located(
    (By.XPATH, MARCAS)))

precos = wait.until(expected_conditions.visibility_of_all_elements_located(
    (By.XPATH, PRECOS)))


for marca, preco in zip(marcas, precos):
    print(marca.text + " " + preco.text)






